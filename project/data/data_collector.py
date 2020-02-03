# importing the requests library
import requests
from requests.auth import HTTPBasicAuth


class DataCollector:

    def getHotelData(self, url):
        # location given here
        location = "delhi technological university"

        # defining a params dict for the parameters to be sent to the API
        PARAMS = {'address': location}

        # sending get request and saving the response as response object
        #r = requests.get(url=url, params=PARAMS)
        r = requests.get(url=url, auth=HTTPBasicAuth('anuradhe.prabhath@gmail.com', 'plutonium_239'))

        # extracting data in json format
        #data = r.json()

        print(r)


if __name__ == "__main__":
    dc = DataCollector()
    # api-endpoint
    URL = "https://distribution-xml.booking.com/2.0/xml/hotels?hotel_ids=10004"
    dc.getHotelData(URL)
