# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['MainTest::test 1'] = GenericRepr('              Timestamp   Device       Sensor   Value\n0   2022-01-01 00:00:00  Device1  Temperature  298.75\n1   2022-01-01 00:05:00  Device1     Humidity    0.70\n2   2022-01-01 00:10:00  Device1  Temperature  299.35\n3   2022-01-01 00:15:00  Device2  Temperature  300.25\n4   2022-01-01 00:20:00  Device2     Humidity    0.65\n5   2022-01-01 00:25:00  Device2  Temperature  301.45\n6   2022-01-01 00:30:00  Device3  Temperature  297.95\n7   2022-01-01 00:35:00  Device3     Humidity    0.75\n8   2022-01-01 00:40:00  Device3  Temperature  299.15\n9   2022-01-01 00:45:00  Device1          CO2  523.00\n10  2022-01-01 00:50:00  Device2          CO2  423.00\n11  2022-01-01 00:55:00  Device3          CO2  623.00')

snapshots['MainTest::test_all_columns 1'] = GenericRepr('              Timestamp   Device       Sensor   Value\n0   2022-01-01 00:00:00  Device1  Temperature  298.75\n1   2022-01-01 00:05:00  Device1     Humidity    0.70\n2   2022-01-01 00:10:00  Device1  Temperature  299.35\n3   2022-01-01 00:15:00  Device2  Temperature  300.25\n4   2022-01-01 00:20:00  Device2     Humidity    0.65\n5   2022-01-01 00:25:00  Device2  Temperature  301.45\n6   2022-01-01 00:30:00  Device3  Temperature  297.95\n7   2022-01-01 00:35:00  Device3     Humidity    0.75\n8   2022-01-01 00:40:00  Device3  Temperature  299.15\n9   2022-01-01 00:45:00  Device1          CO2  523.00\n10  2022-01-01 00:50:00  Device2          CO2  423.00\n11  2022-01-01 00:55:00  Device3          CO2  623.00')

snapshots['MainTest::test_co2 1'] = GenericRepr('              Timestamp   Device Sensor  Value\n9   2022-01-01 00:45:00  Device1    CO2  523.0\n10  2022-01-01 00:50:00  Device2    CO2  423.0\n11  2022-01-01 00:55:00  Device3    CO2  623.0')

snapshots['MainTest::test_humidity 1'] = GenericRepr('             Timestamp   Device    Sensor  Value\n1  2022-01-01 00:05:00  Device1  Humidity   0.70\n4  2022-01-01 00:20:00  Device2  Humidity   0.65\n7  2022-01-01 00:35:00  Device3  Humidity   0.75')

snapshots['MainTest::test_temperature 1'] = GenericRepr('             Timestamp   Device       Sensor   Value\n0  2022-01-01 00:00:00  Device1  Temperature  298.75\n2  2022-01-01 00:10:00  Device1  Temperature  299.35\n3  2022-01-01 00:15:00  Device2  Temperature  300.25\n5  2022-01-01 00:25:00  Device2  Temperature  301.45\n6  2022-01-01 00:30:00  Device3  Temperature  297.95\n8  2022-01-01 00:40:00  Device3  Temperature  299.15')
