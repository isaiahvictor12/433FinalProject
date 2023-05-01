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
    data = {}
    with connection.cursor() as cursor:
        temperature_q = '''SELECT data_record.recording "Y", data_record.record_time "X" 
                           FROM temperature_recording JOIN data_record
                           ON data_record.record_id = temperature_recording.record_id
                           ORDER BY data_record.record_time DESC;'''
        execution_result = cursor.execute(temperature_q)
        data['temperature'] = cursor.fetch_all()
        humidity_q = '''SELECT data_record.recording "Y", data_record.record_time "X" 
                        FROM humidity_recording JOIN data_record
                        ON data_record.record_id = humidity_recording.record_id
                        ORDER BY data_record.record_time DESC;'''
        execution_result = cursor.execute(humidity_q)
        data['humidity'] = cursor.fetch_all()
        light_q = '''SELECT data_record.recording "Y", data_record.record_time "X" 
                     FROM light_recording JOIN data_record
                     ON data_record.record_id = light_recording.record_id
                     ORDER BY data_record.record_time DESC;'''
        execution_result = cursor.execute(light_q)
        data['light'] = cursor.fetch_all()
    file = TEMPLATES['index.tpl']
    return template(file, data=data)
