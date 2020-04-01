#!/usr/bin/bash

# This mini script pulls new data to update the csv file
# Data is from https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv

echo 'Updating'
wget https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv
echo 'Done'
