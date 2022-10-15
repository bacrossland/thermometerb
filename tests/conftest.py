import pytest
from src.thermometerb.thermometer import Thermometer
from src.thermometerb.thermometer_web_socket import ThermometerWebSocket


@pytest.fixture()
def thermometer():
    return Thermometer()


@pytest.fixture()
def thermometer_web_socket():
    return ThermometerWebSocket([])
