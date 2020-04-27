import plotly.figure_factory as ff
import plotly.express as px
import numpy as np
import pandas as pd


def PlotCloropleth(SQLdata, name, date):
	df = pd.DataFrame(SQLdata, columns=['state', 'count'])

	#fips = df['fips'].tolist()
	#values = df['count'].tolist()
	
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
	df['count'] = pd.to_numeric(df['count'], errors='coerce')
	df['state'] = df['state'].apply(lambda x : state_codes[x])
	df['count'] = df['count'].apply(lambda x : np.log(x))
#	fig = ff.create_choropleth(
#		fips=fips, values=values,
#		locationmode="USA-states",
#		binning_endpoints=endpts,
#		colorscale=colorscale,
#		show_state_data=False,
#		show_hover=True, centroid_marker={'opacity': 0},
#		asp=2.9, title='USA by Unemployment %',
#		legend_title='% unemployed'
#	)

	fig = px.choropleth(df, locations='state', color="count", locationmode='USA-states')
	fig.update_layout(
		title_text = 'Log scale of ' + name + ' in US on date ' + date, # Create a Title
		geo_scope='usa',  # Plot only the USA instead of globe
	)
	#fig.layout.template = None
	#fig.show()
	fig.write_image("choropleth.png")