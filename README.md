# CS450 Final

The code repo for Team 1's final project for UH Hilo's spring 2020 CS450.

## Project Overview
This project used Python for the front end and MariaDB for the backend.
For this project, a dataset is stored in a web based database where it 
was queried and plotted. To plot and interact with this data a GUI is 
used to query the web-based database and create graphs from the results.
Python code is largely stored in the 'python' folder and contains the GUI
code as well as the python script used to update the database.

The project's dataset was from <https://github.com/nytimes/covid-19-data/blob/master/us-states.csv>
and is stored in the mariadb folder. This folder contains a bash script which downloads
new iterations of the csv file and removes the existing events from the file by comparing 
the new csv file with the existing one. This new csv file is what's used to populate the 
database. 

Updating the database is a matter of running 
`python3 python/cli-database.py -t mariadb/new-data.csv` from the root folder of this git repo.
Ensure that the credentials are in the cli-database.py file as the program will fail without 
them. A dump of the database is also stored in the mariadb folder, in case the database needs
to be reviewed or restored.

For a more thorough overview of this project, refer to the documentation in the documentation
folder.

## Using the program
The user shouldn't have to interact with the web server, and the program should
work only from the application. For security a Credentials file is used 

## Software and library requirements
This program 

### GUI app
For the front end application Python 3 is used to render the GUI and connect to the 
web database. To use the program please ensure the following libraries are available:
* mysql.connector
* sys
* tkinter

### Plot libraries

## Developers and roles
There were three developers, each with a specific role:
* Emily Risley: Front-end and team lead
* Nicholas Grogg: Web server and database Back-end
* Timothy Kudryn: Data Scientist plot specialist
