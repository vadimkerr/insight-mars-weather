import requests
from core import mars_weather


example_response = {
    "sol_keys": ["1", "2", "3", "4"],
    "1": {
        "AT": {"av": 100, "mn": 50, "mx": 150},
        "HWS": {"av": 5.454, "ct": 150091, "mn": 0.158, "mx": 23.145}
    },
    "2": {"AT": {"av": -100, "mn": -150, "mx": -50}},
    "3": {"AT": {"av": 70, "mn": 50, "mx": 80}},
    "4": {"HWS": {"av": 5.454, "ct": 150091, "mn": 0.158, "mx": 23.145}}
}


def test_api_endpoint_available():
    response = requests.get(mars_weather.QUERY_URL, params=mars_weather.QUERY_PARAMS)
    assert response.status_code == 200


def test_get_response(requests_mock):
    requests_mock.get(mars_weather.QUERY_URL, json=example_response)

    response = mars_weather.get_response(mars_weather.QUERY_URL, mars_weather.QUERY_PARAMS)
    assert type(response) == dict
    assert response == example_response


def test_get_temperature_summaries(requests_mock):
    requests_mock.get(mars_weather.QUERY_URL, json=example_response)

    response = mars_weather.get_response(mars_weather.QUERY_URL, mars_weather.QUERY_PARAMS)
    summaries = mars_weather.get_temperature_summaries(response)

    assert type(summaries) == list
    assert len(summaries) == 3

    assert summaries[0].average_fahrenheit == 100
    assert summaries[0].minimum_fahrenheit == 50
    assert summaries[0].maximum_fahrenheit == 150
