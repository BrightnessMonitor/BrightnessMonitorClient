#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from dbController import *
from getRawData import RCtime
import signal
import time
from brightnessmonitorclient.api_client.update import *

# Interval in seconds the programm is getting new data
measureINTERVAL = 5
# Interval in seconds the programm sends data to server
uploadINTERVAL = 5 * 60
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
            time.sleep(uploadINTERVAL)
            if internet_on():
                pool_sema.acquire()
                success = 0
                for row in retrieve():
                    if not upload(row[1], row[0]):
                        success += 1
                if success < 1:
                    print "Upload successful"
                    drop_recreate_db()
                pool_sema.release()

            if killer.kill_now:
                delete()
                sys.exit(0)


def start():
    thread1 = uploadHandler()
    thread1.start()
    create()
    while True:
        pool_sema.acquire()
        data = RCtime()
        #data = 11
        insert(data)
        pool_sema.release()
        print "Current brightness: %i" % data
        print retrieve()
        time.sleep(measureINTERVAL)

        if killer.kill_now:
            print "Please let the program finish or data loss will occur!"
            break
