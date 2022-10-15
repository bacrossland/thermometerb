"""Class for Thermometer state machine."""
from typing import Any, Optional


class Thermometer:
    """A class that represents a thermometer."""

    BOOL_DEFAULT: bool = False
    HUNDRED_CELSIUS: float = 100.0
    ZERO_CELSIUS: float = 0.0

    def __init__(self, **kwargs: Any):
        """A class that represents a thermometer.
        :keyword boil: Float of temperature threshold in Celsius for boiling.
            Defaults to 100.0ºC.
        :keyword freeze: Float of temperature threshold in Celsius for freezing.
            Defaults to 0.0ºC.
        :keyword full_degree: Bool if a notification should only be sent when a
            threshold has been exceeded by a full degree point (whole number not
            decimal). Default False.
        :keyword increase: Bool if a notification should only be sent if previous temp was an
            increase to reach boil/freeze threshold. Default False.
        :keyword decrease: Bool if a notification should only be sent if previous temp was a
            decrease to reach boil/freeze threshold. Default False.
        :raise ValueError: If boil or freeze temperature data can not be converted to a float.
        """

        self.boil: float = self.HUNDRED_CELSIUS
        self.freeze: float = self.ZERO_CELSIUS
        self.full_degree: bool = self.BOOL_DEFAULT
        self.increase: bool = self.BOOL_DEFAULT
        self.decrease: bool = self.BOOL_DEFAULT
        self.__previous_temp__: float = self.ZERO_CELSIUS
        self.__current_temp__: float = self.ZERO_CELSIUS

        self.__set_data_attributes(**kwargs)

    def __call__(self, temperature: float, **kwargs) -> dict:
        """
        :param temperature: Float of new temperature.
        :keyword boil: Float of temperature threshold in Celsius for boiling.
            Defaults to 100.0ºC.
        :keyword freeze: Float of temperature threshold in Celsius for freezing.
            Defaults to 0.0ºC.
        :keyword full_degree: Bool if a notification should only be sent when a
            threshold has been exceeded by a full degree point (whole number not
            decimal). Default False.
        :keyword increase: Bool if a notification should only be sent if previous temp was an
            increase to reach boil/freeze threshold. Default False.
        :keyword decrease: Bool if a notification should only be sent if previous temp was a
            decrease to reach boil/freeze threshold. Default False.
        :raise ValueError: If boil or freeze temperature data can not be converted to a float.
        :return: Dictionary of temperature in Celcius and Fahrenheit. Includes notification
            if threshold is met.
        """
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
            except ValueError as exc:
                self.__previous_temp__ = cache_previous_temp
                raise ValueError(
                    self.__value_error_msg("current_temp", str(temperature), "float")
                ) from exc
        return self.__current_temp__

    def current_temp_fahrenheit(self) -> float:
        """:return: Float of the current temperature in Fahrenheit."""
        return self.__celsius_to_fahrenheit(self.__current_temp__)

    def previous_temp(self) -> float:
        """:return: Float of the previous temperature in Celsius."""
        return self.__previous_temp__

    def previous_temp_fahrenheit(self) -> float:
        """:return: Float of the previous temperature in Fahrenheit."""
        return self.__celsius_to_fahrenheit(self.__previous_temp__)

    @staticmethod
    def __celsius_to_fahrenheit(temperature: float) -> float:
        """Convert Celsius temperature to Fahrenheit.
        :param temperature: Float of the Celsius temperature to convert.
        :return: Fahrenheit temperature.
        """
        return (temperature * 1.8) + 32.0

    def __set_data_attributes(self, **kwargs: Any):
        """Set data attributes based kwargs supplied.
        :keyword boil: Float of temperature threshold in Celsius for boiling.
            Defaults to 100.0ºC.
        :keyword freeze: Float of temperature threshold in Celsius for freezing.
            Defaults to 0.0ºC.
        :keyword full_degree: Bool if a notification should only be sent when a
            threshold has been exceeded by a full degree point (whole number not
            decimal). Default False.
        :keyword increase: Bool if a notification should only be sent if previous temp was an
            increase to reach boil/freeze threshold. Default False.
        :keyword decrease: Bool if a notification should only be sent if previous temp was a
            decrease to reach boil/freeze threshold. Default False.
        :raise ValueError: If boil or freeze temperature data can not be converted to a float.
        """
        if "boil" in kwargs:
            try:
                self.boil: float = float(kwargs["boil"])
            except ValueError as exc:
                raise ValueError(
                    self.__value_error_msg("boil", kwargs["boil"], "float")
                ) from exc

        if "freeze" in kwargs:
            try:
                self.freeze: float = float(kwargs["freeze"])
            except ValueError as exc:
                raise ValueError(
                    self.__value_error_msg("freeze", kwargs["freeze"], "float")
                ) from exc

        if "full_degree" in kwargs:
            self.full_degree: bool = bool(kwargs["full_degree"])
        if "increase" in kwargs:
            self.increase: bool = bool(kwargs["increase"])
        if "decrease" in kwargs:
            self.decrease: bool = bool(kwargs["decrease"])

    @staticmethod
    def __value_error_msg(location: str, value: str, cast_type: str) -> str:
        """
        Format an error message for ValueError.
        :param location: String of the data attribute.
        :param value: String of the value being converted.
        :param cast_type: String of the type being cast to.
        :return: String of formatted error message.
        """
        return f"Can not convert {location} value {value} to a {cast_type}."
