#Author: Emily Risley 
#Date: April 2020

import plotly.express as px
import numpy as np
import pandas as pd

#takes list of tuples containing state name (long form) and count (as returned from a sql query)
# name of the type of data, and date the data is associated with
# creates and saves figure to app directory
def PlotCloropleth(SQLdata, name, date):
	df = pd.DataFrame(SQLdata, columns=['state', 'count'])
	
	state_codes = {
		'District of Col' : 'dc','Mississippi': 'MS', 'Oklahoma': 'OK', 
		'Delaware': 'DE', 'Minnesota': 'MN', 'Illinois': 'IL', 'Arkansas': 'AR', 
		'New Mexico': 'NM', 'Indiana': 'IN', 'Maryland': 'MD', 'Louisiana': 'LA', 
		'Idaho': 'ID', 'Wyoming': 'WY', 'Tennessee': 'TN', 'Arizona': 'AZ', 
		'Iowa': 'IA', 'Michigan': 'MI', 'Kansas': 'KS', 'Utah': 'UT', 
		'Virginia': 'VA', 'Oregon': 'OR', 'Connecticut': 'CT', 'Montana': 'MT', 
		'California': 'CA', 'Massachusetts': 'MA', 'West Virginia': 'WV', 
		'South Carolina': 'SC', 'New Hampshire': 'NH', 'Wisconsin': 'WI',
		'Vermont': 'VT', 'Georgia': 'GA', 'Guam': 'GU','North Dakota': 'ND', 
		'Pennsylvania': 'PA', 'Florida': 'FL', 'Alaska': 'AK', 'Kentucky': 'KY', 
		'Hawaii': 'HI', 'Nebraska': 'NE', 'Missouri': 'MO', 'Ohio': 'OH', 
		'Alabama': 'AL', 'Rhode Island': 'RI', 'South Dakota': 'SD', 'American Samoa':'AS', 
		'Colorado': 'CO', 'New Jersey': 'NJ', 'Washington': 'WA', 'Virgin Islands' : 'VI', 
		'North Carolina': 'NC', 'New York': 'NY', 'Texas': 'TX', 'Puerto Rico': 'PR', 
		'Nevada': 'NV', 'Maine': 'ME', 'Northern Marian' :'MP'}
		
	#change state names to abbreviation
	df['state'] = df['state'].apply(lambda x : state_codes[x])
	
	#scale counts logarithmically
	df['count'] = pd.to_numeric(df['count'], errors='coerce')
	df['scaled_count'] = df['count'].apply(lambda x : np.log(x))

	#plot cloropleth on us states choropleth
	fig = px.choropleth(df, locations='state', color="scaled_count", locationmode='USA-states')
	fig.update_layout(
		title_text = 'Log scale of ' + name + ' in US on date ' + date, # Create a Title
		geo_scope='usa',  # Plot only the USA instead of globe
	)
	
	fig.write_image(name + "-" + date + "-choropleth.png")