import pytest
from core import mars_weather


@pytest.fixture
def temperature_summary() -> mars_weather.TemperatureSummary:
    temperature_summary = mars_weather.TemperatureSummary(
        sol=1337,
        average_fahrenheit=47,
        minimum_fahrenheit=43,
        maximum_fahrenheit=50
    )

    return temperature_summary


def test_fahrenheit_to_celsius():
    assert mars_weather.TemperatureSummary.fahrenheit_to_celsius(0) == -17.778
    assert mars_weather.TemperatureSummary.fahrenheit_to_celsius(100) == 37.778
    assert mars_weather.TemperatureSummary.fahrenheit_to_celsius(-100) == -73.333


def test_summary_init(temperature_summary: mars_weather.TemperatureSummary):
    assert temperature_summary.average_fahrenheit == 47
    assert temperature_summary.minimum_fahrenheit == 43
    assert temperature_summary.maximum_fahrenheit == 50

    assert temperature_summary.average_celsius == 8.333
    assert temperature_summary.minimum_celsius == 6.111
    assert temperature_summary.maximum_celsius == 10


def test_summary_str(temperature_summary: mars_weather.TemperatureSummary):
    assert str(temperature_summary) == 'Sol 1337:\n' \
            '\tAverage temperature: 8.333 °C\n' \
            '\tMinimum temperature: 6.111 °C\n' \
            '\tMaximum temperature: 10.0 °C'
