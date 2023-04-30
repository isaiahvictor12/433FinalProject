from sensornetwork import HOST_INFO
from sensornetwork.db import DATABASE
import mysql.connector

__version__ = "1.0.0"

_USERNAME = "sensor"

_database_connection = mysql.connector.connect(
    host=HOST_INFO[0],
    user=_USERNAME,
    database=DATABASE
)

sensor_cursor = _database_connection.cursor()

RECORD_DELAY: int = 10
