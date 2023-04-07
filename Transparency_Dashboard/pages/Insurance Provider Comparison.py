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

# Set Page design
st.set_page_config(layout="wide", page_title="Insurance Provider Comparison")

st.markdown("# Insurance Provider Comparison")
st.sidebar.header("Insurance Provider Comparison")
st.write('This tool is used to compare the prices between insurance providers.')

# Import DataFrame of Provider Information
df = pd.read_csv('Data/Final Dataset Cleaned.csv')

# Function to Create Descriptive Stats (Average, Min, Max)
def create_metric(data):
	# Laying out page for Descriptive Statistics
	row1_1, row1_2, row1_3, row1_4 = st.columns((1, 1, 1, 1))
	with row1_1:
		st.metric(label="Average", value='$'+str(round(data['Negotiated Rate'].mean(),2)))
	with row1_2:
		st.metric(label="Maximum", value='$'+str(round(data['Negotiated Rate'].max(),2)))
	with row1_3:
		st.metric(label="Minimum", value='$'+str(round(data['Negotiated Rate'].min(),2)))
	with row1_4:
		st.metric(label="Median", value='$'+str(round(data['Negotiated Rate'].median(),2)))


## Procedure Selector
with st.sidebar:
	procedure_option = st.selectbox(
    	'Which Procedure would you like to see?',
    	(df['Procedure Description'].unique()))
#st.write('You selected:', procedure_option)

## Negotiation Type Selector
#negotiation_option = st.multiselect(
#    'Which Negotiation would you like to see?',
#    (df['Negotiation Type'].unique()))
#st.write('You selected:', procedure_option)

## Filter by Procedure and Insurance Provider
#page_uno_filter = df[(df['Negotiation Type'] == negotiation_option) & (df['Procedure Description'] == procedure_option)]
page_uno_filter = df[(df['Procedure Description'] == procedure_option)]

## Calculate Average
calc_avg = page_uno_filter.groupby(['Insurance Provider'])['Negotiated Rate'].mean().reset_index()
calc_avg.rename(columns = {'Negotiated Rate' : 'Average Negotiated Rate'}, inplace=True)

# Create Metrics line
create_metric(page_uno_filter)

# Create extra line
st.write('***')
## Bar Chart Comparing 3 Insurance Providers
st.bar_chart(calc_avg, x='Insurance Provider', y= 'Average Negotiated Rate', height=500)

# Create distplot with custom bin_size
#fig = ff.create_distplot(calc_avg)
#st.plotly_chart(fig, use_container_width=True)



