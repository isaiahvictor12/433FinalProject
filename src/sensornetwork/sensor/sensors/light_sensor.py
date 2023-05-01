from sensornetwork.sensor.sensors.sensor import Sensor
import RPi.GPIO as GPIO


class LightSensor(Sensor):

    def __init__(self, pin):
        super().__init__(0.1)
        self.pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def _read_data(self):
        read = GPIO.input(self.pin)
        if read == GPIO.HIGH:
            return 1.0
        return 0.0
