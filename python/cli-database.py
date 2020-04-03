#!/usr/bin/python3

import argparse
import mysql.connector

"""
This is a script used to populate a remote database
"""

parser = argparse.ArgumentParser()
parser.add_argument("-t", action='store', dest='textfile', required=True, help="Use text file T")
args = parser.parse_args()

# The name of the file
fileName = args.textfile

# MySQL connection information
cnx = mysql.connector.connect(user='project',password='',database='cs450',host='')
cur = cnx.cursor()

ff = open(fileName)
line = ff.readline()

while line:
    date,state,fips,cases,deaths = line.split(',')
    insert                       = ("""INSERT INTO project(date,state,fips,cases,deaths) VALUES(%s,%s,%s,%s,%s)""")
    data_value                   = (date,state,fips,cases,deaths)
    cur.execute(insert,data_value)
    cnx.commit()
    line                         = ff.readline()
ff.close()

# Close MySQL connection
cur.close()
cnx.close()
