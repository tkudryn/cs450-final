#!/usr/bin/bash

# This mini script pulls new data to update the csv file
# Data is from https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

# Move previous iteration to old file
mv us-states.csv us-states-old.csv

# Download newer version of file
echo 'Updating'
wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

# Remove first line of file
echo 'Removing title row from file'
sed -i -e 1d us-states.csv

# Create new file based on difference between the two
echo 'Comparing old and new files, creating new-data.csv'
grep -F -x -v -f us-states-old.csv us-states.csv > new-data.csv

echo 'Done'
