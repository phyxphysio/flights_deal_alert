import settings
import requests
from set_dates import set_dates
from sheet_data import get_sheet_data

sheet_data = get_sheet_data()

def set_prices(percent=settings.FLIGHT_PRICE_PERCENTAGE):
    # Get cheapest flight for each destination

    date_from, date_to = set_dates()

    for row in sheet_data:
        if "iataCode" in row.keys():
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
            response = requests.get(
                settings.SEARCH_URL, params=seach_params, headeres=settings.SEARCH_HEADERS
            )
            if response.status_code == 200:
                flights = response.json()

                # Set lowest price to % of current price
                row["lowestPrice"] = flights["data"][0]["price"] * (
                    percent / 100
                )

                # Update lowest price in Google Sheet
                edit_row_url = settings.SHEET_URL + row['id']

                body = {"price": row}
                put_headers = {
                    "Content-Type": "application/json",
                }
                put_response = requests.put(
                    edit_row_url, json=body, SEARCH_HEADERS=put_headers
                )
                if put_response.status_code != 200:
                    print(put_response.status_code, put_response.text)
                else:
                    print(
                        f'Successfully added trigger price of {row['lowestPrice']} for {row['city']}.'
                    )
            else:
                print(f"Error {response.status_code, response.text}")

if __name__ =='__main__':
    set_prices()
