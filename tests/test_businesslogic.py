import datetime
import zoneinfo

from main import calculate_time_to_reach_hb
from opendata import Journey
from opendata.models import Stop, Station, Prognosis

BERLIN = zoneinfo.ZoneInfo("Europe/Berlin")
NOW = datetime.datetime(2025, 1, 1, 12, 0, tzinfo=BERLIN)
MAX_VALUE = 9999


def test_calculate_time_to_reach_hb_no_target():
    """Ensure that a tram that never reaches HB returns MAX_VALUE"""
    journey = Journey(
        name="Tram 7",
        category="T",
        number=7,
        to="Zoo",
        stop=Stop(
            station=Station(id=0, name="Erasmusplatz"),
            prognosis=Prognosis(arrival=None, departure=None),
        ),
        passList=[
            Stop(
                station=Station(id=1, name="Central"),
                prognosis=Prognosis(
                    arrival=NOW + datetime.timedelta(minutes=10),
                    departure=None,
                ),
            ),
        ],
    )

    assert calculate_time_to_reach_hb(journey, NOW) == MAX_VALUE


def test_calculate_time_to_reach_hb_valid_target():
    """Ensure that a tram that reaches HB returns the correct time"""
    journey = Journey(
        name="Tram 50",
        category="T",
        number=50,
        to="Auzelg",
        stop=Stop(
            station=Station(id=0, name="Waidfussweg"),
            prognosis=Prognosis(arrival=None, departure=None),
        ),
        passList=[
            Stop(
                station=Station(id=1, name="Zürich, Sihlquai/HB"),
                prognosis=Prognosis(
                    arrival=NOW + datetime.timedelta(minutes=10),
                    departure=None,
                ),
            ),
        ],
    )

    assert calculate_time_to_reach_hb(journey, NOW) == 10
