import json
import pathlib

import requests

import opendata.models as models
from abc import ABC, abstractmethod

TEST_DATA = pathlib.Path(__file__).parent / 'testdata'


class Client(ABC):
    @abstractmethod
    def get_stationboard(self, station_name: str) -> models.StationBoardResponse:
        """ Fetches the current StationBoard for station_name """
        raise NotImplementedError


class FakeClient(Client):
    def get_stationboard(self, station_name: str):
        with open(TEST_DATA / 'stationboard_waidfussweg.json') as fo:
            data = json.load(fo)
        return models.StationBoardResponse.model_validate(data)


class OpenDataClient(Client):
    base_url = 'http://transport.opendata.ch/v1'

    def get_stationboard(self, station_name: str) -> models.StationBoardResponse:
        data = requests.get(f'{self.base_url}/stationboard?station={station_name}&limit=10').json()
        return models.StationBoardResponse.model_validate(data)
