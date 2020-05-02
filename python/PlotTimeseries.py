#Author: Emily Risley 
#Date: April 2020

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

#takes list of tuples as returned form database query, and name of data type
#creates and saves time series plot based on data
def PlotTimeseries(SQLdata, name):
	df = pd.DataFrame(SQLdata, columns=['state', 'date', 'count'])

	#make data column a date time type
	df['date']= pd.to_datetime(df['date'])
	df = df.set_index('date')
	
	fig, ax = plt.subplots(figsize=(12, 12))

	# Add x-axis and y-axis
	ax.bar(df.index.values,
		df['count'],
		color='purple')

	# Set title and labels for axes
	ax.set(xlabel="Date",
		ylabel=name,
		title=name + " in " + df['state'][0] + " from beginning of reporting period to now")

	# Define the date format
	date_form = DateFormatter("%m-%d")
	ax.xaxis.set_major_formatter(date_form)

	plt.savefig( name + "-" + df['state'][0] + '-timeseries.png')