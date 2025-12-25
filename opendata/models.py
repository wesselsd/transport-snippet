import pydantic
from typing import List
from datetime import datetime, date, time


class Station(pydantic.BaseModel):
    id: int
    name: str


class Prognosis(pydantic.BaseModel):
    """ A prognosis contains "realtime" information on the
    status of a connection checkpoint. """
    arrival: datetime
    departure: datetime


class Stop(pydantic.BaseModel):
    """ A checkpoint represents an arrival or
    a departure point (in time and space) of a connection. """
    station: Station
    prognosis: Prognosis


class Journey(pydantic.BaseModel):
    """ The actual transportation of a section, e.g. a bus or
    a train between two stations. """
    name: str
    category: str  # transportation category, like T for Tram
    number: int  # tram number, like 13
    to: str
    stop: Stop


class StationBoard(pydantic.BaseModel):
    """
    The response of a stationboard query, as described here:
    https://transport.opendata.ch/docs.html#stationboard
    """

    station: Station
    stationboard: List[Journey]
