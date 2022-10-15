import pytest
from src.thermometerb.thermometer_web_socket import ThermometerWebSocket


def test_thermometer_web_socket_defaults(thermometer_web_socket):
    with pytest.raises(TypeError, match="Source needs to be of type"):
        ThermometerWebSocket("str")

    assert type(thermometer_web_socket) == ThermometerWebSocket
    assert thermometer_web_socket.boil == 100.0
    assert thermometer_web_socket.freeze == 0.0
