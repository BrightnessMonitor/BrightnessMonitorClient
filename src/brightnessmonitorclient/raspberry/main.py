#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
from dbController import *
import getRawData
import signal
import time
from brightnessmonitorclient.api_client.update import *

# Interval in seconds the programm is getting new data
measureINTERVAL = 5
# Interval in seconds the programm sends data to server
uplpadINTERVAL = 5 * 60
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


class myThread(threading.Thread):
    temp_data = None

    def run(self):
        while True:
            time.sleep(uplpadINTERVAL)
            if internet_on():
                pool_sema.acquire()
                temp_data = retrieve()
                drop_recreate_db()
                pool_sema.release()
                print "upload data"
                for row in temp_data:
                    upload(row[1], row[0])
            if killer.kill_now:
                sys.exit(0)


if __name__ == '__main__':
    thread1 = myThread()
    thread1.start()
    create()
    while True:
        pool_sema.acquire()
        insert(getRawData.RCtime(11))
        pool_sema.release()
        time.sleep(measureINTERVAL)

        if killer.kill_now:
            break