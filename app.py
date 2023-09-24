import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
