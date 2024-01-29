import requests
import settings

def get_sheet_data():

    response = requests.get(settings.SHEET_URL)

    if response.status_code == 200:
        rdata = response.json()

    else:
        print(f"Error {response.status_code, response.text}")

    return rdata['prices']
