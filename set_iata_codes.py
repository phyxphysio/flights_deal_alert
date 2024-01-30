import settings
from sheet_data import get_sheet_data
import requests


def set_iata_codes():
    sheet_data = get_sheet_data()
    for row in sheet_data:
        if "city" in row.keys():
            city_params = {"term": row["city"]}
            city_data = requests.get(
                settings.LOC_URL, city_params, headers=settings.KIWI_API_HEADERS
            )
            data = city_data.json()
            row["iataCode"] = data["locations"][0]["code"]

    for row in sheet_data:
        if row["city"]:
            # edit_row_url = settings.SHEET_URL + str(row["id"])
            edit_row_url = f'https://api.sheety.co/802fe87a122e46509e9a7371a51672a4/copyOfFlightDeals/prices/{row['id']}'

            body = {"price": row}
            put_headers = {
                "Content-Type": "application/json",
            }
            put_response = requests.put(edit_row_url, json=body, headers=put_headers)
            if put_response.status_code != 200:
                print(put_response.status_code, put_response.text)
            else:
                print(
                    f'Successfully set IATA Code for {row['city']} to  {row['iataCode']}.'
                )


if __name__ == "__main__":
    set_iata_codes()
