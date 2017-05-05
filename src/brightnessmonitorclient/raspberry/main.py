#!/usr/bin/env python

from dbController import *
import getRawData
import signal
import time

INTERVAL = 5


class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.kill_now = True

if __name__ == '__main__':
  killer = GracefulKiller()
  create()
  while True:
      #only for test purpose
      #insert(11)
      insert(getRawData.RCtime(11))
      print retrieve()
      time.sleep(INTERVAL)
      if killer.kill_now:
          delete()
          break

  print "End of the program. I was killed gracefully :)"
