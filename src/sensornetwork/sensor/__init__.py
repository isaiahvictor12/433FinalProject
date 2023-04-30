from sensornetwork import HOST_INFO
from sensornetwork.db import DATABASE
import mysql.connector

__version__ = "1.0.0"

_USERNAME = "sensor"

connection = mysql.connector.connect(
    host=HOST_INFO[0],
    user=_USERNAME,
    database=DATABASE
)

RECORD_DELAY: int = 10
