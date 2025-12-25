import datetime
import zoneinfo

from opendata import FakeClient, Journey, OpenDataClient

MAX_VALUE = 9999


def calculate_time_to_reach_hb(journey: Journey, now: datetime.datetime) -> int:
    """Returns the estimated time to reach Sihlquai/HB using a given Journey,
    returns 9999 if the given Journey never reaches Sihlquai/HB."""
    target = "Zürich, Sihlquai/HB"
    result = MAX_VALUE
    for stop in journey.passList:
        if stop.station.name == target:
            result = (stop.prognosis.arrival - now).total_seconds()//60
    return result


def find_fastest_journey(journeys: list[Journey], now: datetime.datetime) -> Journey:
    fastest = MAX_VALUE
    result = journeys[0]
    for journey in journeys:
        time_to_reach_hb = calculate_time_to_reach_hb(journey, now)
        if time_to_reach_hb < fastest:
            fastest = time_to_reach_hb
            result = journey
    return result


def main():
    client = OpenDataClient()
    res = client.get_stationboard("Meierhofplatz")
    now = datetime.datetime.now(tz=zoneinfo.ZoneInfo("Europe/Berlin"))

    fastest_journey = find_fastest_journey(res.stationboard, now)
    print("The fastest tram from Meierhofplatz to Zurich hb:")
    print(f"Tram number {fastest_journey.number} to {fastest_journey.to}")
    print(f"Leaves {fastest_journey.stop.station.name} at {fastest_journey.stop.prognosis.arrival}")
    checkpoint = [cp for cp in fastest_journey.passList if cp.station.name == "Zürich, Sihlquai/HB"][0]
    print(f"arrives at {checkpoint.station.name} at {checkpoint.prognosis.arrival}")


if __name__ == '__main__':
    main()
