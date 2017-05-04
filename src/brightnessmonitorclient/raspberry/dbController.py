#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import time

con = None
cur = None
sqlite_file = 'test.db'


def create_db():
    con = lite.connect(sqlite_file)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS data")
        cur.execute("CREATE TABLE data (time REAL, data INTEGER);")
        print "Table created"
        con.commit()


def commit_to_db(rawdata):
    try:
        con = lite.connect(sqlite_file)
        cur = con.cursor()
        #inserts time and raw data into database
        #time represents the number of seconds since Jan 1, 1970 00:00:00
        cur.execute("INSERT INTO data VALUES (?, ?)", (time.time(), rawdata))
        con.commit()
    except lite.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        con.close()