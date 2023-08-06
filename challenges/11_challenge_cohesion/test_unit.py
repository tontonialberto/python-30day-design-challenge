from typing import Any
import unittest
from after import celsius_to_kelvin, compensate_co2_sensor_bias, percentage, validate_option, process_row
from pandas import Series


CSV_HEADER = ["Timestamp", "Device", "Sensor", "Value"]


def create_row(device: str, sensor: str, value: float) -> "Series[Any]":
    return Series(
        data=["2022-01-01 00:00:00", device, sensor, value],
        index=CSV_HEADER,
    )


PROCESSOR_FUNCS = {
    "CO2": [compensate_co2_sensor_bias],
    "Humidity": [percentage],
    "Temperature": [celsius_to_kelvin],
}


class Test(unittest.TestCase):
    def test_validate_option(self) -> None:
        validate_option("All")
        validate_option("Temperature")
        validate_option("Humidity")
        validate_option("CO2")

    def test_validate_option_invalid(self) -> None:
        self.assertRaises(Exception, lambda _: validate_option("dummy"))

    def test_process_temperature(self) -> None:
        row = create_row(
            device="Device1",
            sensor="Temperature",
            value=25.6,
        )
        processed_row = process_row(row, PROCESSOR_FUNCS)
        expected_temperature = 25.6 + 273.15
        actual_temperature = processed_row["Value"]
        self.assertEqual(expected_temperature, actual_temperature)

    def test_process_co2(self) -> None:
        row = create_row(
            device="Device1",
            sensor="CO2",
            value=300,
        )
        processed_row = process_row(row, PROCESSOR_FUNCS)
        expected = 300 + 23
        actual = processed_row["Value"]
        self.assertEqual(expected, actual)

    def test_process_humidity(self) -> None:
        row = create_row(
            device="Device1",
            sensor="Humidity",
            value=98,
        )
        processed_row = process_row(row, PROCESSOR_FUNCS)
        expected = 98 / 100
        actual = processed_row["Value"]
        self.assertEqual(expected, actual)
