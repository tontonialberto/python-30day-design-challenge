from functools import partial
from typing import Any, Callable, Dict, Iterable, List
import pandas as pd


SENSOR_TYPES = ["Temperature", "Humidity", "CO2"]


SENSOR_FILTERS = ["All", *SENSOR_TYPES]


ConverterFunc = List[Callable[[float], float]]


SensorProcessors = Dict[str, ConverterFunc]
"""Map a sensor to a list of post-processing functions."""


def validate_option(option: str) -> None:
    """Validate CSV filter option. Raise an exception if not valid."""
    assert (
        option in SENSOR_FILTERS
    ), f'Option not valid, should be ({", ".join(SENSOR_FILTERS)}) {option} given!'


"""Data conversion functions."""


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def percentage(value: float) -> float:
    """Convert value in 0-100 range to 0-1 range."""
    return value / 100


def compensate_co2_sensor_bias(co2_biased: float) -> float:
    """
    Args:

    - co2_biased: The raw CO2 value coming from the biased sensor.
    """
    return co2_biased + 23


def process_row(
    row: "pd.Series[Any]", processors: SensorProcessors
) -> "pd.Series[Any]":
    """
    Apply the data transformation to the given measurement row.

    Args:

    - row: The row to be processed.

    Returns:

    - The processed row, or None if the given row doesn't contain a known measurement.
    """
    sensor: str = row["Sensor"]
    known_processors: Iterable[str] = processors.keys()
    if sensor in known_processors:
        for processor in processors[sensor]:
            row["Value"] = processor(row["Value"])
    else:
        raise Exception(f"Unknown sensor '{sensor}'")
    return row


def process_data(data: pd.DataFrame, processors: SensorProcessors) -> pd.DataFrame:
    """
    Args:

    - data: Input data to be converted.
    - processors: For each sensor type, a pipeline of the conversion operations.

    Returns:

    - A DataFrame containing only rows coming from known sensor types. Each measurement is processed through its pipeline.
    """
    processed_data: List["pd.Series[Any]"] = []
    for _, row in data.iterrows():
        processed_row = process_row(row, processors)
        processed_data.append(processed_row)

    processed_data_single = pd.DataFrame(data=processed_data)
    return processed_data_single


DataFilter = Callable[[pd.DataFrame], pd.DataFrame]


def filter_data(data: pd.DataFrame, filterers: Iterable[DataFilter]) -> pd.DataFrame:
    for filterer in filterers:
        data = filterer(data)
    return data


"""Filter functions."""


def filter_by_sensor_type(sensor_type: str, data: pd.DataFrame) -> pd.DataFrame:
    """
    Filter measurements by sensor type.

    Args:

    - sensor_type: The type of sensor measurement.
    - data: DataFrame of sensor measurements.

    Returns:

    - Only the rows in `data` belonging to the given `sensor_type`.
    """
    if sensor_type in ("Temperature", "Humidity", "CO2"):
        data = data.loc[data["Sensor"] == sensor_type]
    return data


def filter_exclude_unknown_sensors(sensor_types: List[str], data: pd.DataFrame) -> pd.DataFrame:
    """Filter out rows coming from unknown sensors."""
    data = data.loc[data["Sensor"].isin(sensor_types)]
    return data


ROWS_PROCESSORS: SensorProcessors = {
    "CO2": [compensate_co2_sensor_bias],
    "Humidity": [percentage],
    "Temperature": [celsius_to_kelvin],
}


def process_csv(option: str, csv_path: str) -> pd.DataFrame:
    validate_option(option)

    data: pd.DataFrame = pd.read_csv(csv_path) 
    processed_data = filter_data(
        data,
        [
            partial(filter_by_sensor_type, option),
            partial(filter_exclude_unknown_sensors, SENSOR_TYPES),
        ],
    )
    processed_data = process_data(processed_data, ROWS_PROCESSORS)
    return processed_data


def main() -> None:
    try:
        result = process_csv("All", "sensor_data.csv")
        print(result)
    except AssertionError as err:
        print(err)


if __name__ == "__main__":
    main()
