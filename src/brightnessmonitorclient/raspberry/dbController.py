#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import time


sqlite_file = 'test.db'
con = None
cur = None


def drop_recreate_db():
    con = lite.connect(sqlite_file)
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS data")
        print "Table dropped"
        cur.execute("CREATE TABLE data (time REAL, data INTEGER);")
        print "Table created"
        con.commit()


def create():
    con = lite.connect(sqlite_file)
    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS data (time REAL, data INTEGER);")
        print "Table created"
        con.commit()


def insert(rawdata):
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

def retrieve():
    data = []
    con = lite.connect(sqlite_file)
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM data')
        table = cur.fetchall()
        for row in table:
            data.append(row)
    return data