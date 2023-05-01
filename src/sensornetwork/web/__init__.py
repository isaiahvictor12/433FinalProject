from sensornetwork import HOST_INFO
from sensornetwork.db import DATABASE
from sensornetwork.web.templates import TEMPLATES
from bottle import template, route
import mysql.connector


__version__ = "1.0.0"
_USERNAME = "webserver"
PORT = 8080

connection = mysql.connector.connect(
    host=HOST_INFO[0],
    user=_USERNAME,
    database=DATABASE
)

# Home Page25
@route('/')
def index():
    file = TEMPLATES['index.tpl']
    return template(file, (None, ))
