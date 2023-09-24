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
