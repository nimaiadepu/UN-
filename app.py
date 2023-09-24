import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# Define your API key
api_key = "YOUR_API_KEY_HERE"

# Define the endpoint URL for population data (you can find the correct endpoint on the UN's API documentation)
population_url = "https://api.un.org/data/population"

# Define parameters (e.g., year, country, indicator) for your request
params = {
    "timePeriod": "2022",
    "country": "all",
    "indicator": "SP_POP_TOTL",
    "apiKey": api_key,
}

# Make the API request
response = requests.get(population_url, params=params)

# Parse the JSON response
data = response.json()

# Extract relevant data
population_data = data['value']
# Title of the web app
st.title("UN Data Analysis")

# Sidebar for user input
indicator = st.sidebar.selectbox("Select Indicator", ["Population", "GDP", "Economy"])

# Display data based on user selection
if indicator == "Population":
    st.header("Population Data")
    # Use Pandas DataFrame for population data
    df = pd.DataFrame(population_data)
    st.write(df)
    
    # Create a histogram
    st.header("Population Distribution")
    plt.hist(df['value'], bins=20)
    st.pyplot()

elif indicator == "GDP":
    # Similar to the population section but for GDP data
    pass

elif indicator == "Economy":
    # Similar to the population section but for economic data
    pass

# Optionally, you can add more features like time series analysis, filtering by country, etc.
