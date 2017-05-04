#!/usr/bin/env python

import dbController
import getRawData

def start():
    dbController.create_db()
    dbController.commit_to_db(getRawData.RCtime(11))
    print dbController.retrieve()