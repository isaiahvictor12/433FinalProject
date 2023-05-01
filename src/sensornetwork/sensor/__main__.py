import asyncio
from sensornetwork.sensor.sensors.ds18b20 import DS18B20
from sensornetwork.sensor.sensors.humidity_sensor import HumiditySensor
from sensornetwork.sensor.sensors.light_sensor import LightSensor
from sensornetwork.sensor import connection, RECORD_DELAY


def record_temperature(temp_sensor):
    temperature = temp_sensor.celsius
    with connection.cursor() as cursor:
        query = "CALL record_temperature(%s);"
        cursor.execute(query, (temperature, ))


def record_light(light_sensor):
    light = light_sensor.get_reading()
    with connection.cursor() as cursor:
        query = "CALL record_light(%s);"
        cursor.execute(query, (light, ))


def record_humidity(humidity_sensor):
    humidity = humidity_sensor.get_reading()
    with connection.cursor() as cursor:
        query = "CALL record_humidity(%s);"
        cursor.execute(query, (humidity, ))


async def main():
    temp_sensor = DS18B20()
    light_sensor = LightSensor(19)
    humidity_sensor = HumiditySensor(22)

    while True:

        record_temperature(temp_sensor)
        record_light(light_sensor)
        record_humidity(humidity_sensor)

        await asyncio.sleep(RECORD_DELAY)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
