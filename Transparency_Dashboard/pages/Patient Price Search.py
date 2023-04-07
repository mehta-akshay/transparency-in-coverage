# Importing packages
import os
import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st
import haversine as hs
from geopy.geocoders import Nominatim 

# Set Page design
st.set_page_config(layout="wide", page_title="Patient Price Comparison", page_icon="📊")

st.markdown("# Patient Price Comparison")
st.sidebar.header("Patient Price Comparison")
st.write('This is an interactive tool to show the best prices for medical procedures within a designated area.')

# Loading Dataframe
@st.cache_resource
def load_data():
    path = "Data/Final Dataset Cleaned.csv"
    #if not os.path.isfile(path):
    #    path = f"https://github.com/{Rest of URL}/{path}"
    data = pd.read_csv(path)
    return data

# Filter data using input widgets
@st.cache_data
def filterdata(df, slider, option1, option2):

    return df[df['Distance'] == slider]

# @st.cache_data
# def topfilterdata(df,)

# Import DataFrame into app
df = load_data()

#df = pd.read_csv('Data/Final Dataset Cleaned.csv')

# Import city information
city_df = pd.read_csv('Data/cities-coordinates.csv', usecols=['City','lat','lon'])
city_df.sort_values('City',inplace=True)

# Input widgets for Distance Based Dashboard
# https://docs.streamlit.io/library/api-reference/widgets

#!!! Put in different file and reference back here???
# Function to calculate distance from selected city
def get_distance(df_row):
    calc_distance = hs.haversine([lat,lng],[df_row['Latitude'],df_row['Longitude']],unit='mi')
    return calc_distance

# Initialize that long/lat to the variables
lat,lng = 0,0

# Create sidebar with input widgets
with st.sidebar:

	# st.session_state.my_slider = 25

	# slider = st.slider(
    # 	label='Choose a Value', min_value=1,
    # 	max_value=50, value=25, key='my_slider')

	## City Selector
	city_option = st.selectbox(
	    'Which City would you like to see?',
	    (city_df['City']))
	#st.write('You selected:', city_option)

	## Insurance Selector
	insurance_option = st.selectbox(
	    'Which Insurance Provider do you use?',
	    (df['Insurance Provider'].unique()))
	#st.write('You selected:', insurance_option)

	## Procedure Selector
	procedure_option = st.selectbox(
	    'Which Procedure would you like to see?',
	    (df['Procedure Description'].unique()))
	#st.write('You selected:', procedure_option)

	## Slider for Distance
	distance_slider = st.slider('What distance are you looking for?', 0, 100, 25)
	#st.write('looking ', distance_slider, ' miles away')





# Filter by Procedure and Insurance Provider
page_dos_filter = df[(df['Insurance Provider'] == insurance_option) & (df['Procedure Description'] == procedure_option)]

# Drop duplicates
page_dos_filter.drop_duplicates(inplace=True)

# Set value of lat,lng
lat, lng = city_df.loc[city_df['City'] == city_option].lat.values[0] , city_df.loc[city_df['City'] == city_option].lon.values[0]

# Run function for distance calculation
page_dos_filter['Distance (mi)'] = page_dos_filter.apply(get_distance,axis =1)

# Filter by distance from slider
page_dos_filter = page_dos_filter[(page_dos_filter['Distance (mi)'] <= distance_slider)]

# Sort values by least expensive
page_dos_filter.sort_values('Negotiated Rate', inplace=True)


# Create Column subset for filtered set
page_dos_columns = ['Negotiated Rate','Provider Name','City','Address','Distance (mi)']

# Filtered dataset
page_dos_filter_top = page_dos_filter[page_dos_columns]
page_dos_filter_top = page_dos_filter_top \
						.iloc[:20] \
						.reset_index(drop=True) \
						.style \
							.format(precision=2) \
							.hide_index()


# Display Subset 

lowest_price_header_text = '20 Lowest Prices for ' + ':blue[' + procedure_option + ']' + ' within ' + str(distance_slider) + ' miles of ' + city_option
st.subheader(lowest_price_header_text)

st.dataframe(page_dos_filter_top)

# Laying out page for Descriptive Statistics
row1_1, row1_2, row1_3, row1_4 = st.columns((1, 1, 1, 1))


# Create Descriptive Stats (Average, Min, Max)
with row1_1:
	st.metric(label="Average", value='$'+str(round(page_dos_filter['Negotiated Rate'].mean(),2)))
	#st.write('**Average:** $' , str(round(page_dos_filter['Negotiated Rate'].mean(),2)))

with row1_2:
	st.metric(label="Maximum", value='$'+str(round(page_dos_filter['Negotiated Rate'].max(),2)))
	#st.write('**Maximum:** $' , str(round(page_dos_filter['Negotiated Rate'].max(),2)))

with row1_3:
	st.metric(label="Minimum", value='$'+str(round(page_dos_filter['Negotiated Rate'].min(),2)))
	#st.write('**Minimum:** $' , str(round(page_dos_filter['Negotiated Rate'].min(),2)))

with row1_4:
	st.metric(label="Median", value='$'+str(round(page_dos_filter['Negotiated Rate'].median(),2)))
	#st.write('**Median:** $' , str(round(page_dos_filter['Negotiated Rate'].median(),2)))

#st.metric(label="Average", value=str(round(page_dos_filter['Negotiated Rate'].mean(),2)), delta="1.2 °F")

# Create Bar Chart
st.bar_chart(page_dos_filter_top, x='Provider Name', y='Negotiated Rate', height=500)

# Rename Lat/Lng for map function
page_dos_filter.rename(columns={'Latitude':'lat','Longitude':'lon'},inplace=True)

# Create Map
st.map(page_dos_filter)





