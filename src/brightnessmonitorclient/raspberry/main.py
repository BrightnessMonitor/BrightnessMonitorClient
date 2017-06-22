#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from dbController import *
from getRawData import RCtime
import signal
import time
from brightnessmonitorclient.api_client.update import *
from timeConvert import convertback
from daylight import *

# Interval in seconds the programm is getting new data
measureINTERVAL = 5
# Interval in seconds the programm sends data to server
uploadINTERVAL = 300
# Semaphore for database read/write
pool_sema = threading.BoundedSemaphore(value=1)


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True


killer = GracefulKiller()


class uploadHandler(threading.Thread):
    temp_data = None

    def run(self):
        while True:
            print "Wait %i seconds for next upload" % uploadINTERVAL
            for i in range(uploadINTERVAL):

                upload_time_left = uploadINTERVAL - i
                # print every 10 secounds the remaining time
                if upload_time_left % 10 == 0:
                    print("time left: %i" % upload_time_left)

                time.sleep(1)
                if killer.kill_now:
                    break

            if internet_on():
                pool_sema.acquire()

                fail = 0
                print "Upload ",
                for row in retrieve():
                    if not upload(row[1], convertback(row[0])):
                        fail += 1
                    print "*",
                print "\n"

                if fail < 1:
                    print "Upload successful"
                    drop_recreate_db()
                    pool_sema.release()
            else:
                print("no connection to the server")

            if killer.kill_now:
                delete()
                sys.exit(0)


def start():
    thread1 = uploadHandler()
    thread1.start()
    create()
    setLocation()
    while True:
        while checkDaylight():
            pool_sema.acquire()
            data = RCtime()
            insert(data)
            pool_sema.release()
            print "Current brightness: %i" % data
            time.sleep(measureINTERVAL)

            if killer.kill_now:
                print "Please let the program finish or data loss will occur!"
