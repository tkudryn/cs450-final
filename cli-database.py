#!/usr/bin/python3

import argparse
import mysql.connector

'''
If repurposing, the only changes that need to be made are to the
insert statements, and
the data_value variable

Optionally, rename the Table if statements to line up with table being used
'''

parser = argparse.ArgumentParser()
parser.add_argument("-a", action='store', dest='table', required=True, help="Add to table A")
parser.add_argument("-t", action='store', dest='textfile', required=True, help="Use text file T")
args = parser.parse_args()

# The name of the file
fileName = args.textfile
Table    = args.table

# MySQL connection information
cnx = mysql.connector.connect(user='',password='',database='CS421',host='localhost')
cur = cnx.cursor()

ff = open(fileName)
line = ff.readline()

# If table flag is B for brand table
if Table == 'B':
    while line:
        line.split()
        a,b,c               = line.split()
        insert              = ("""INSERT INTO brand(make,brand_worth,public) VALUES(%s,%s,%s)""")
        data_value          = (a,b,c)
        cur.execute(insert,data_value)
        cnx.commit()
        line                = ff.readline()
    ff.close()

# If table flag is BT for Body Type table
elif Table == 'BT':
    while line:
        line.split()
        a,b,c,d,e           = line.split()
        insert              = ("""INSERT INTO body_type(platform_code,construction,shape,drive,suspension) VALUES(%s,%s,%s,%s,%s)""")
        data_value          = (a,b,c,d,e)
        cur.execute(insert,data_value)
        cnx.commit()
        line                = ff.readline()
    ff.close()

# If table flag is C for car table
elif Table == 'C':
    while line:
        line.split()
        a,b,c,d,e,f,g       = line.split()
        insert              = ("""INSERT INTO car(model,make,price,platform_code,drive,aggregate_review,autonomous) VALUES(%s,%s,%s,%s,%s,%s,%s)""")
        data_value          = (a,b,c,d,e,f,g)
        cur.execute(insert,data_value)
        cnx.commit()
        line                = ff.readline()
    ff.close()


# If table flag is CO for Cost of Ownership table
elif Table == 'CO':
    while line:
        line.split()
        a,b,c,d,e           = line.split()
        insert              = ("""INSERT INTO costofownership(model,make,maintenance,depreciation,recalls) VALUES(%s,%s,%s,%s,%s)""")
        data_value          = (a,b,c,d,e)
        cur.execute(insert,data_value)
        cnx.commit()
        line                = ff.readline()
    ff.close()

# If table flag is E for Engine table
elif Table == 'E':
    while line:
        line.split()
        a,b,c,d,e,f,g       = line.split()
        insert              = ("""INSERT INTO engine(engine_code,cylinder_count,engine_type,hp,torque,fuel_type,induction) VALUES(%s,%s,%s,%s,%s,%s,%s)""")
        data_value          = (a,b,c,d,e,f,g)
        cur.execute(insert,data_value)
        cnx.commit()
        line                = ff.readline()
    ff.close()

# If table flag is JP for Joint Project table
elif Table == 'JP':
    while line:
        line.split()
        a,b,c,d,e,f,g,h,i   =line.split()
        insert              = ("""INSERT INTO jointproject(model,make1,make2,engine_code,platform_code,critic_score,customer_score,average_score,autonomous) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)""")
        data_value          = (a,b,c,d,e,f,g,h,i)
        cur.execute(insert,data_value)
        cnx.commit()
        line                = ff.readline()
    ff.close()

# If table flag is R for Review table
elif Table == 'R':
    while line:
        line.split()
        a,b,c               = line.split()
        insert              = ("""INSERT INTO review(model,critic_score,customer_score) VALUES(%s,%s,%s)""")
        data_value          = (a,b,c)
        cur.execute(insert,data_value)
        cnx.commit()
        line                = ff.readline()
    ff.close()

# If table flag is T for Tech table
elif Table == 'T':
    while line:
        line.split()
        a,b,c,d,e,f         = line.split()
        insert              = ("""INSERT INTO tech(model,infotainment,proximity_sensor,auto_braking,adc,autonomous) VALUES(%s,%s,%s,%s,%s,%s)""")
        data_value          = (a,b,c,d,e,f)
        cur.execute(insert,data_value)
        cnx.commit()
        line                = ff.readline()
    ff.close()


# If table flag is UE for Uses Engine table
elif Table == 'UE':
    while line:
        line.split()
        a,b                 = line.split()
        insert              = ("""INSERT INTO usesengine(engine_code,model) VALUES(%s,%s)""")
        data_value          = (a,b)
        cur.execute(insert,data_value)
        cnx.commit()
        line                = ff.readline()
    ff.close()

# Fail state for invalid options
else:
    print("Invalid parameter")

# Close MySQL connection
cur.close()
cnx.close()
