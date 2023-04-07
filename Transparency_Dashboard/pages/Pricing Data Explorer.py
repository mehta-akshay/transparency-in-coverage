# Importing packages
import os
import altair as alt
import numpy as np
import pandas as pd
import pydeck as pdk
import streamlit as st
import haversine as hs
from geopy.geocoders import Nominatim


# Import DataFrame of Provider Information

df = pd.read_csv('Data/Final Dataset Cleaned.csv')

# Function to Create Descriptive Stats (Average, Min, Max)
## Define in separate file and import into file?
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

# Explorer 

from streamlit_extras.dataframe_explorer import dataframe_explorer

explorer_df = df[['Insurance Provider','Procedure Description','City','Address','Negotiated Rate','Negotiation Type','Billing Code Type']]
filtered_df = dataframe_explorer(explorer_df)
st.dataframe(filtered_df, use_container_width=True)


create_metric(filtered_df)

# # Create Descriptive Stats (Average, Min, Max)
# st.write('Average: $' , str(round(filtered_df['Negotiated Rate'].mean(),2)))
# st.write('Maximum: $' , str(round(filtered_df['Negotiated Rate'].max(),2)))
# st.write('Minimum: $' , str(round(filtered_df['Negotiated Rate'].min(),2)))
# st.write('Median: $' , str(round(filtered_df['Negotiated Rate'].median(),2)))
