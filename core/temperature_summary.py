from dataclasses import dataclass, field


@dataclass
class TemperatureSummary:
    sol: int

    average_fahrenheit: float
    minimum_fahrenheit: float
    maximum_fahrenheit: float

    average_celsius: float = field(init=False)
    minimum_celsius: float = field(init=False)
    maximum_celsius: float = field(init=False)

    def __post_init__(self):
        self.average_celsius = TemperatureSummary.fahrenheit_to_celsius(self.average_fahrenheit)
        self.minimum_celsius = TemperatureSummary.fahrenheit_to_celsius(self.minimum_fahrenheit)
        self.maximum_celsius = TemperatureSummary.fahrenheit_to_celsius(self.maximum_fahrenheit)

    def __str__(self):
        return f'Sol {self.sol}:\n' \
            f'\tAverage temperature: {self.average_celsius} °C\n' \
            f'\tMinimum temperature: {self.minimum_celsius} °C\n' \
            f'\tMaximum temperature: {self.maximum_celsius} °C'

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit_temperature: float) -> float:
        celsius_temperature = (fahrenheit_temperature - 32) / 1.8
        return round(celsius_temperature, ndigits=3)
