# Importing packages
import os
import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st
import haversine as hs
from geopy.geocoders import Nominatim
import plotly.figure_factory as ff
import pydeck as pdk

# Set Page design
st.set_page_config(layout="wide", page_title="Map Overview")

st.markdown("# Map Overview")
st.write('This map shows the number of records that came from each city.')

# Loading Dataframe
@st.cache_resource
def load_data():
    path = "Data/Final Dataset Cleaned.csv"
    #if not os.path.isfile(path):
    #    path = f"https://github.com/{Rest of URL}/{path}"
    data = pd.read_csv(path)
    return data

# Import DataFrame into app
df = load_data()

# Import city information
city_df = pd.read_csv('Data/cities-coordinates.csv', usecols=['City','lat','lon'])
city_df.sort_values('City',inplace=True)

# Create a datset for histogram
@st.cache_data
def histdata(dataframe, cities):
	grouped_cities = dataframe.groupby('City', as_index=False).agg(Count=pd.NamedAgg(column="City", aggfunc="count"))
	grouped_cities = grouped_cities.join(cities.set_index('City'),on=['City'],how='inner')
	return grouped_cities


regroup = histdata(df,city_df)


st.pydeck_chart(pdk.Deck(
	map_style=None,
	initial_view_state=pdk.ViewState(
		latitude=regroup['lat'].mean(),
		longitude=regroup['lon'].mean(),
        zoom=6,
        pitch=45,
	),
	layers = 
		pdk.Layer(
		    "ColumnLayer",
		    data=regroup,
		    get_position=["lon", "lat"],
		    get_elevation="Count",
		    elevation_scale=1,
		    radius=6500,
		    get_fill_color=[255,215,0, 140],
		    pickable=True,
		    auto_highlight=True,
		),
		tooltip = {"html": "<b>{City}</b> has <b>{Count}</b> records in dataset.",
			"style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},}
	)
)


st.markdown("#### Table of cities and count of records")
st.write(regroup[['City','Count']], use_container_width=True)