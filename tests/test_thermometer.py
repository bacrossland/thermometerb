import pytest
from src.thermometerb.thermometer import Thermometer


def test_thermometer_defaults(thermometer):
    assert type(thermometer) == Thermometer
    assert thermometer.boil == 100.0
    assert thermometer.freeze == 0.0


def test_thermometer_keyword_boil():
    with pytest.raises(ValueError, match="Can not convert boil value"):
        Thermometer(boil="boil")
    gauge_boil_float = Thermometer(boil=2.0)
    gauge_boil_int = Thermometer(boil=3)
    gauge_boil_str = Thermometer(boil="4")
    assert type(gauge_boil_float) == Thermometer
    assert gauge_boil_float.boil == 2.0
    assert type(gauge_boil_int) == Thermometer
    assert gauge_boil_int.boil == 3.0
    assert type(gauge_boil_str) == Thermometer
    assert gauge_boil_str.boil == 4.0


def test_thermometer_keyword_freeze():
    with pytest.raises(ValueError, match="Can not convert freeze value"):
        Thermometer(freeze="freeze")
    gauge_freeze_float = Thermometer(freeze=1.0)
    gauge_freeze_int = Thermometer(freeze=2)
    gauge_freeze_str = Thermometer(freeze="3")
    assert type(gauge_freeze_float) == Thermometer
    assert gauge_freeze_float.freeze == 1.0
    assert type(gauge_freeze_int) == Thermometer
    assert gauge_freeze_int.freeze == 2.0
    assert type(gauge_freeze_str) == Thermometer
    assert gauge_freeze_str.freeze == 3.0


def test_current_temp(thermometer):
    with pytest.raises(ValueError, match="Can not convert value"):
        thermometer.current_temp("temp")

    assert thermometer.current_temp() == 0.0
    thermometer.current_temp(2.0)
    assert thermometer.current_temp() == 2.0
    thermometer.current_temp(3)
    assert thermometer.current_temp() == 3.0
    thermometer.current_temp("4")
    assert thermometer.current_temp() == 4.0


def test_previous_temp(thermometer):
    assert thermometer.previous_temp() == 0.0
    thermometer.current_temp(1.0)
    thermometer.current_temp(2.0)
    assert thermometer.previous_temp() == 1.0


def test_current_temp_fahrenheit(thermometer):
    assert thermometer.current_temp_fahrenheit() == 32.0
    thermometer.current_temp(10.0)
    assert thermometer.current_temp_fahrenheit() == 50.0


def test_previous_temp_fahrenheit(thermometer):
    assert thermometer.previous_temp_fahrenheit() == 32.0
    thermometer.current_temp(10.0)
    thermometer.current_temp(11.0)
    assert thermometer.previous_temp_fahrenheit() == 50.0
