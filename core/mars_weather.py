#!/usr/bin/env python3

import os
from typing import List
import requests

# To be able to run either as python -m core and python core/mars_weather.py
if __package__ is None:
    from temperature_summary import TemperatureSummary
else:
    from core.temperature_summary import TemperatureSummary


API_KEY = os.environ['API_KEY']
QUERY_URL = 'https://api.nasa.gov/insight_weather/'
QUERY_PARAMS = {
    'api_key': API_KEY,
    'feedtype': 'json',
    'ver': '1.0'
}


def get_response(url: str, params: dict) -> dict:
    response = requests.get(url, params=params)
    return response.json()


def get_temperature_summaries(response: dict) -> List[TemperatureSummary]:
    sols = response['sol_keys']
    summaries = []
    for sol in sols:
        sol_info = response[sol]

        temperature_info = sol_info.get('AT')
        if not temperature_info:
            continue

        summary = TemperatureSummary(
            sol=sol,
            average_fahrenheit=temperature_info['av'],
            minimum_fahrenheit=temperature_info['mn'],
            maximum_fahrenheit=temperature_info['mx'],
        )
        summaries.append(summary)

    return summaries


def main():
    api_response = get_response(QUERY_URL, QUERY_PARAMS)
    temperature_summaries = get_temperature_summaries(api_response)

    for temperature_summary in temperature_summaries:
        print(temperature_summary)


if __name__ == '__main__':
    main()
