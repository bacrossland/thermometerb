from .thermometer import Thermometer
from typing import Any


class ThermometerWebSocket(Thermometer):
    """A class that represents a thermometer that reads and notifies to a web socket.
    This class takes input of temperature data."""

    def __init__(self, source: list, **kwargs: Any):
        """A class that represents a thermometer that reads and notifies to a web socket.

        :param source: List of float Celsius temperature readings.
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
        if isinstance(source, list):
            self.__source__: list = source
        else:
            raise TypeError("Source needs to be of type list...")
        super().__init__(**kwargs)
