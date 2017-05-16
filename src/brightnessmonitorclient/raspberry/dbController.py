#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import time


sqlite_file = '/var/db/BrightnessMonitor.sqlite'
table = 'data'
vartime = 'time'
vardata = 'data'
con = None
cur = None


def create():
    ''' 
    
    Creates database table 'data' with Integer values time and data

    '''
    try:
        con = lite.connect(sqlite_file)
        cur = con.cursor()
    except lite.Error, e:
        print "create(): Error %s:" % e.args[0]
        sys.exit(1)
    with con:
        cur.execute("CREATE TABLE IF NOT EXISTS {table} ({time} INTEGER, {data} INTEGER);".
                    format(table=table, time=vartime, data=vardata))
        con.commit()


def drop_recreate_db():
    delete()
    create()


def insert(rawdata):
    '''
    Inserts data into data table, adds timestamp to data
    Args:
        rawdata: data to be inserted

    '''
    try:
        con = lite.connect(sqlite_file)
        cur = con.cursor()
        # inserts time and raw data into database
        # time represents the number of seconds since Jan 1, 1970 00:00:00
        cur.execute("INSERT INTO {table} VALUES ({time}, {data})".
                    format(table=table, time=int(time.time()), data= rawdata))
        con.commit()
    except lite.Error, e:
        print "insert(): Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        con.close()


def retrieve():
    data = []
    try:
        con = lite.connect(sqlite_file)
        cur = con.cursor()
    except lite.Error, e:
        print "retrieve(): Error %s:" % e.args[0]
        sys.exit(1)
    with con:
        cur.execute('SELECT * FROM data')
        table = cur.fetchall()
        for row in table:
            data.append(row)
    return data


def delete():
    try:
        con = lite.connect(sqlite_file)
        cur = con.cursor()
    except lite.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    with con:
        cur.execute("DROP TABLE IF EXISTS data")