from mailer import send_email 
import settings 
from set_dates import set_dates
from sheet_data import get_sheet_data
import requests


sheet_data = get_sheet_data()

def compare_prices():
    # Get lowest price
    date_from, date_to = set_dates()

    for row in sheet_data:
        if "lowestPrice" in row.keys():
            seach_params = {
                "fly_from": settings.LOCAL_CITY_CODE,
                "fly_to": row["iataCode"],
                "curr": settings.CURRENCY_CODE,
                "date_from": date_from,
                "date_to": date_to,
                "nights_in_dst_from": settings.MIN_TRIP_LENGTH,
                "nights_in_dst_to": settings.MAX_TRIP_LENGTH,
                "limit": 1,
            }

            # Get current price of flight
            response = requests.get(
                settings.SEARCH_URL, params=seach_params, headers=settings.KIWI_API_HEADERS
            )
            if response.status_code == 200:
                #Parse API Response 
                flights = response.json()
                price = flights["data"][0]["price"]
                cutoff_price = row["lowestPrice"]
                city_from = flights["data"][0]["cityFrom"]
                city_to = flights["data"][0]["cityTo"]
                departure = flights['data'][0]["local_departure"][:10]
                home = flights['data'][0]['route'][-1]['local_arrival'][:10]
                print(f'Evaluating {city_from} to {city_to}...')

                # Compare current price to lowest price
                if price < cutoff_price:
                    print('Low price! Sending alert...')
                    discount = round(100-((price/cutoff_price)*100),2)
                    # Send email
                    send_email(
                        f'There is a flight from {city_from} to {city_to} for {price} AUD. \n It leaves on {departure} and returns on {home}. This is {discount}% lower than your cutoff prie of {cutoff_price}.'
                    )
                else:
                    print('No deal!')
            else:
                print(response.status_code, response.text)

if __name__ =='__main__':
    compare_prices()
