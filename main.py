import datetime
import zoneinfo

from opendata import FakeClient, Journey, OpenDataClient, Client

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


def example1(client: Client):
    """ Get the next connection from Meierhofplatz to Zurich HB """
    print("Example 1: Meierhofplatz -> Zurich HB")
    res = client.get_stationboard("Meierhofplatz")
    now = datetime.datetime.now(tz=zoneinfo.ZoneInfo("Europe/Berlin"))

    fastest_journey = find_fastest_journey(res.stationboard, now)

    print("The fastest tram from Meierhofplatz to Zurich hb:")
    print(f"Tram number {fastest_journey.number} to {fastest_journey.to}")
    print(f"Leaves {fastest_journey.stop.station.name} at {fastest_journey.stop.prognosis.arrival}")
    checkpoint = [cp for cp in fastest_journey.passList if cp.station.name == "Zürich, Sihlquai/HB"][0]
    print(f"arrives at {checkpoint.station.name} at {checkpoint.prognosis.arrival}")


def example2(client: Client):
    """ Find the tram that will arrive soonest at any station in Zurich """

    print("Example 2: Soonest arrival")
    locations = client.get_locations("Zurich")
    earliest = None
    earliest_station = None
    for location in locations:
        stationboard = client.get_stationboard(location.name)
        current_arrival = stationboard.stationboard[0].stop.prognosis.arrival
        earliest_station = stationboard
        if earliest is None or earliest > current_arrival:
            earliest = current_arrival

    print(f"The earliest arrival is at {earliest}, on {earliest_station.station.name}. "
          f"It is line {earliest_station.stationboard[0].number}.")


def main():
    # client = OpenDataClient()
    client = FakeClient()
    example1(client)
    print()
    example2(client)


if __name__ == '__main__':
    main()
