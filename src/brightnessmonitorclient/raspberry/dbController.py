#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import time


sqlite_file = 'test.db'
con = None
cur = None


def create():
    try:
        con = lite.connect(sqlite_file)
        cur = con.cursor()
    except lite.Error, e:
        print "create(): Error %s:" % e.args[0]
        sys.exit(1)
    with con:
        cur.execute("CREATE TABLE IF NOT EXISTS data (time INTEGER, data INTEGER);")
        print "create(): Table created"
        con.commit()


def drop_recreate_db():
    try:
        con = lite.connect(sqlite_file)
        cur = con.cursor()
    except lite.Error, e:
        print "drop_recreate_db(): Error %s:" % e.args[0]
        sys.exit(1)
    with con:
        cur.execute("DROP TABLE IF EXISTS data")
        print "drop_recreate_db(): Table dropped"
        cur.execute("CREATE TABLE data (time INTEGER, data INTEGER);")
        print "drop_recreate_db(): Table created"
        con.commit()


def insert(rawdata):
    try:
        con = lite.connect(sqlite_file)
        cur = con.cursor()
        #inserts time and raw data into database
        #time represents the number of seconds since Jan 1, 1970 00:00:00
        cur.execute("INSERT INTO data VALUES (?, ?)", (int(time.time()), rawdata))
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
        print "delete(): Table deleted"