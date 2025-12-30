import pydantic
from typing import List, Optional
from datetime import datetime, date, time


class Station(pydantic.BaseModel):
    id: int
    name: Optional[str] = ""


class Prognosis(pydantic.BaseModel):
    """ A prognosis contains "realtime" information on the
    status of a connection checkpoint. """
    arrival: Optional[datetime]
    departure: Optional[datetime]


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
    passList: List[Stop]


class StationBoardResponse(pydantic.BaseModel):
    """
    The response of a stationboard query, as described here:
    https://transport.opendata.ch/docs.html#stationboard
    """

    station: Station
    stationboard: List[Journey]


class Location(pydantic.BaseModel):
    name: str


class LocationResponse(pydantic.BaseModel):
    """
    The response of a locations query, as described here:
    https://transport.opendata.ch/docs.html#location
    """
    stations: list[Location]
