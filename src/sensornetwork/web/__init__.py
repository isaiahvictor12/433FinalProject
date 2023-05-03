from sensornetwork import HOST_INFO
from sensornetwork.db import DATABASE
from sensornetwork.web.static import STATIC_FILES
from sensornetwork.web.templates import TEMPLATES
from bottle import template, route, static_file
from json import dumps
import mysql.connector


__version__ = "1.0.0"
_USERNAME = "webserver"
PORT = 8080

connection = mysql.connector.connect(
    host=HOST_INFO[0],
    user=_USERNAME,
    database=DATABASE
)

# Static files
@route('/static/<path:path>')
def serve_static_files(path):
    print(f"Serving static file ${path}")
    stream = STATIC_FILES.get(path)
    if stream:
        return stream.read_bytes()
    else:
        return 404

# Home Page25
@route('/')
def index():
    data = {}
    with connection.cursor(buffered=True) as cursor:
        temperature_q = '''SELECT data_record.recording "Y", data_record.record_time "X" 
                           FROM temperature_recording JOIN data_record
                           ON data_record.record_id = temperature_recording.record_id
                           ORDER BY data_record.record_time DESC;'''
        execution_result = cursor.execute(temperature_q)
        results = [row for row in cursor.fetchall()]
        labels = [row[1].strftime('%Y-%m-%d %H:%M:%S') for row in results]
        data['labels'] = labels
        y = [f"{row[0]:.2f}" for row in results]
        data['temperature'] = y.copy()
        humidity_q = '''SELECT data_record.recording "Y", data_record.record_time "X" 
                        FROM humidity_recording JOIN data_record
                        ON data_record.record_id = humidity_recording.record_id
                        ORDER BY data_record.record_time DESC;'''
        execution_result = cursor.execute(humidity_q)
        results = [row for row in cursor.fetchall()]
        y = [f"{row[0]:.2f}" for row in results]
        data['humidity'] = y.copy()
        light_q = '''SELECT data_record.recording "Y", data_record.record_time "X" 
                     FROM light_recording JOIN data_record
                     ON data_record.record_id = light_recording.record_id
                     ORDER BY data_record.record_time DESC;'''
        execution_result = cursor.execute(light_q)
        results = [row for row in cursor.fetchall()]
        y = [f"{row[0]:.2f}" for row in results]
        data['light'] = y.copy()

    file = TEMPLATES['index.tpl']
    return template(file.read_text(encoding='utf-8'), data=dumps(data), safe=True)
