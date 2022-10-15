from typing import Any, Optional


class Thermometer:
    """A class that represents a thermometer."""

    HUNDRED_CELSIUS: float = 100.0
    ZERO_CELSIUS: float = 0.0

    def __init__(self, **kwargs: Any):
        """A class that represents a thermometer.
        :keyword boil: Float of temperature threshold in Celsius for boiling. Defaults to 100.0ºC.
        :keyword freeze: Float of temperature threshold in Celsius for freezing. Defaults to 0.0ºC.
        :keyword full_degree: Bool if a notification should only be sent when a threshold has been exceeded by a full
            degree point (whole number not decimal). Default False.
        :keyword increase: Bool if a notification should only be sent if previous temp was an increase to reach
            boil/freeze threshold. Default False.
        :keyword decrease: Bool if a notification should only be sent if previous temp was a decrease to reach
            boil/freeze threshold. Default False.
        :raise ValueError: If boil or freeze temperature data can not be converted to a float.
        :raise TypeError: If source is not the correct type.
        """

        if "boil" in kwargs.keys():
            try:
                self.boil: float = float(kwargs["boil"])
            except ValueError:
                raise ValueError(
                    f"Can not convert boil value {kwargs['boil']} to a float."
                )
        else:
            self.boil: float = self.HUNDRED_CELSIUS

        if "freeze" in kwargs.keys():
            try:
                self.freeze: float = float(kwargs["freeze"])
            except ValueError:
                raise ValueError(
                    f"Can not convert freeze value {kwargs['freeze']} to a float."
                )
        else:
            self.freeze: float = self.ZERO_CELSIUS

        self.__previous_temp__: float = self.ZERO_CELSIUS
        self.__current_temp__: float = self.ZERO_CELSIUS

    def __call__(self, temperature: float, **kwargs) -> dict:
        """"""
        return {}

    def current_temp(self, temperature: Optional[float] = None) -> float:
        """Set the current temperature.
        :param temperature: Float of the current temperature.
        :return: Float of the current temperature in Celsius.
        :raise ValueError: If temperature can not be converted to a float.
        """
        if temperature:
            cache_previous_temp: float = self.__previous_temp__
            self.__previous_temp__ = self.__current_temp__
            try:
                self.__current_temp__ = float(temperature)
            except ValueError:
                self.__previous_temp__ = cache_previous_temp
                raise ValueError(f"Can not convert value {temperature} to a float.")
        return self.__current_temp__

    def current_temp_fahrenheit(self) -> float:
        """:return: Float of the current temperature in Fahrenheit."""
        return self.__celsius_to_fahrenheit__(self.__current_temp__)

    def previous_temp(self) -> float:
        """:return: Float of the previous temperature in Celsius."""
        return self.__previous_temp__

    def previous_temp_fahrenheit(self) -> float:
        """:return: Float of the previous temperature in Fahrenheit."""
        return self.__celsius_to_fahrenheit__(self.__previous_temp__)

    def __celsius_to_fahrenheit__(self, temperature: float) -> float:
        """Convert Celsius temperature to Fahrenheit.
        :param temperature: Float of the Celsius temperature to convert.
        :return: Fahrenheit temperature.
        """
        return (temperature * 1.8) + 32.0
