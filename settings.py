# Set your preferences here 

import os 

# Enter your trip preferences in days 
MIN_TRIP_LENGTH = 14
MAX_TRIP_LENGTH = 30
SOONEST_DEPARTURE = 14
LATEST_DEPARTURE = 240

# When settings lowest prices, this is the percentage below current prices you'd like the lowest price to be 
FLIGHT_PRICE_PERCENTAGE = 10

#Sheety API Integration 
SHEET_URL = os.getenv('SHEET_URL')

LOCAL_CITY_CODE = "SYD"
CURRENCY_CODE = "AUD"

# Kiwi.com API Integration 
SEARCH_URL = "https://api.tequila.kiwi.com/v2/search"
KIWI_API_HEADERS = {"apikey": os.getenv("API_KEY")}
LOC_URL = 'https://api.tequila.kiwi.com/locations/query'
