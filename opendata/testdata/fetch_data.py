import json

import requests
import pydantic


stationboard_url = 'http://transport.opendata.ch/v1/stationboard?station=Waidfussweg&limit=10'
locations_url = 'http://transport.opendata.ch/v1/locations?query=Zurich'

response = requests.get(stationboard_url).json()
with open('stationboard_waidfussweg.json', 'w') as fo:
    json.dump(response, fo, indent=4)

response = requests.get(locations_url).json()
with open('locations.json', 'w') as fo:
    json.dump(response, fo, indent=4)
