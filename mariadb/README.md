# MariaDB

These files are used to create and populate the database with the relevant
data. Use the .sql file to create the tables and use the .csv file with
the cli-database.py file to populate the database.

The data for this database is from <https://github.com/nytimes/covid-19-data/blob/master/us-states.csv>

The update script uses wget to pull a new version of the file from the github repo. Use this
with the cli-script to update the database with the new data. This script will create a file based
on what's new in the csv compared to what's in the old csv file. The new-data.csv file can be used to
append new values to the database.
