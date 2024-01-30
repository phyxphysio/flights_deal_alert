Flights Deal Alert

This application sends you an email alert when the price of a light to your chosen destination drops below a certain price.

All you need to start is a Google Sheet with the columns: 'City', 'IATA Code', and 'Lowest Price'. You can leave the IATA code and Lowest Price columns blank and populate them with this program.

After your Google Sheet has been made, fill in your trip preferences and API endpoints/keys in the settings.py file

To set IATA codes, run python set_iata_codes.py

To set lowest prices, run set_prices.py

To compare your lowest price with the current price and recieve an email alert for any deals, periodically run compare_prices.py
