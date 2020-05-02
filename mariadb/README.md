# MariaDB

These files are used to create and populate the database with the relevant
data. Use the .sql file to create the tables and use the .csv file with
the cli-database.py file to populate the database.

The data for this database is from <https://github.com/nytimes/covid-19-data/blob/master/us-states.csv>

The update script uses wget to pull a new version of the file from the github repo. Use this
with the cli-script to update the database with the new data. This script will create a file based
on what's new in the csv compared to what's in the old csv file. The new-data.csv file can be used to
append new values to the database.

## Files 
new-data.csv, New data to add to the database <br>
us-states.csv, The complete data set <br>
us-states-old.csv, an older version of the data set for a back up <br>
us-states-headers.csv, A version of the data set that retains the headers <br>
cs450.sql, an sqldump of the database. Functions as submittable code and as a backup of the database <br>
update-data.sh, a bash script used to download new versions of the csv file and parse the new data from
the old data.
