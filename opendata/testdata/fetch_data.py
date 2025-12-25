import json

import requests
import pydantic


base_url = 'http://transport.opendata.ch/v1/stationboard?station=Waidfussweg&limit=10'

response = requests.get(base_url).json()
with open('stationboard_waidfussweg.json', 'w') as fo:
    json.dump(response, fo, indent=4)
