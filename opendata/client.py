import json
import pathlib

import requests

import models
from abc import ABC, abstractmethod

TEST_DATA = pathlib.Path(__file__).parent / 'testdata'


class Client(ABC):
    @abstractmethod
    def get_stationboard(self, station_name: str) -> models.StationBoard:
        """ Fetches the current StationBoard for station_name """
        raise NotImplementedError


class FakeClient(Client):
    def get_stationboard(self, station_name: str):
        with open(TEST_DATA / 'stationboard_waidfussweg.json') as fo:
            data = json.load(fo)
        return models.StationBoard.model_validate(data)


class OpenDataClient(Client):
    base_url = 'http://transport.opendata.ch/v1'

    def get_stationboard(self, station_name: str) -> models.StationBoard:
        data = requests.get(f'{self.base_url}/stationboard?station={station_name}&limit=10').json()
        return models.StationBoard.model_validate(data)


if __name__ == '__main__':

    answer = FakeClient().get_stationboard("waidfussweg")
    # answer = OpenDataClient().get_stationboard("waidfussweg")

    for station in answer.stationboard:
        print(station.stop.prognosis.departure)
