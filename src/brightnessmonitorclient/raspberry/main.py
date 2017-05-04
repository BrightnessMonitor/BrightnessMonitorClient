#!/usr/bin/env python

import dbController
#import getRawData

def start():
    #rawdata = getRawData.RCtime(11)
    sampledata = 436

    #dbController.create_db()
    dbController.commit_to_db(sampledata)