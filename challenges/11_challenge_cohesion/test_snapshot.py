from snapshottest import TestCase  # type: ignore

from after import process_csv
from constants import CSV_FILE_PATH


class MainTest(TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.maxDiff = None

    def test_all_columns(self) -> None:
        result = process_csv("All", CSV_FILE_PATH)
        self.assertMatchSnapshot(result)  # type: ignore

    def test_temperature(self) -> None:
        result = process_csv("Temperature", CSV_FILE_PATH)
        self.assertMatchSnapshot(result)  # type: ignore

    def test_humidity(self) -> None:
        result = process_csv("Humidity", CSV_FILE_PATH)
        self.assertMatchSnapshot(result)  # type: ignore

    def test_co2(self) -> None:
        result = process_csv("CO2", CSV_FILE_PATH)
        self.assertMatchSnapshot(result)  # type: ignore
