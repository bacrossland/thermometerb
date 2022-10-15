"""Tests for the ThermometerWebSocket class"""
import pytest
from src.thermometerb.thermometer_web_socket import ThermometerWebSocket


def test_thermometer_web_socket_defaults(thermometer_web_socket):
    """Test for ThermometerWebSocket data attribute defaults being set on object instantiation."""
    with pytest.raises(TypeError, match="Source needs to be of type"):
        ThermometerWebSocket("str")

    assert isinstance(thermometer_web_socket, ThermometerWebSocket)
    assert thermometer_web_socket.boil == 100.0
    assert thermometer_web_socket.freeze == 0.0
