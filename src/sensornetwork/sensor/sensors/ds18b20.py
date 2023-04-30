from glob import glob
from time import perf_counter
import logging
import re
import subprocess
from sensornetwork.sensor.sensors.sensor import Sensor


def _modprobe(module: str) -> bool:
    '''This function calls the modprobe command with the module as an argument.
    Be careful with this.

    :param module: Name of module to load.
    :type module: str
    :return: True if the module was successfully loaded, false otherwise.
    :rtype: bool
    '''
    try:
        completion = subprocess.run(['modprobe', module])
        completion.check_returncode()
    except subprocess.SubprocessError:
        logging.error("Kernal module %s could not be loaded.",
                      module, stack_info=True)
        return False
    else:
        return True


# Load the temperature sensors
gpio_status = _modprobe("w1-gpio")
therm_status = _modprobe("w1-therm")
if not (gpio_status and therm_status):
    raise ImportError((
        "DS18B20 Kernal Modules could not be loaded, "
        "cannot import DS18B20 module."
    ))

COMMAND_REGEX: re.Pattern = re.compile(r"t=(\d+)")


class DS18B20(Sensor):
    """Wrapper for the DS18B20 Temperature Sensor."""

    # Per the data sheet: 12-bit resolution conversion time takes max 750 ms.
    # https://www.analog.com/media/en/technical-documentation/data-sheets/DS18B20.pdf
    MAX_DELAY: float = 1_000 / 750

    def __init__(self, count: int = 0):
        super().__init__(DS18B20.MAX_DELAY)

        # This is where the sensors will be
        base_dir = "/sys/bus/w1/devices/"
        device_folder = glob(base_dir + "28*")[count]
        self._device_file = device_folder + "/w1_slave"

    def _read_raw(self) -> str:
        """Probe the sensor and return the result. If the sensor has been
        probed too recently, return a cached result.

        :return: The raw string result, with newlines joined by a space.
        :rtype: str
        """
        result: str = None
        with open(self._device_file, "r") as f:
            result = " ".join(f.readlines())
        return result

    def _read_temp(self) -> int:
        """Read the raw data and get the temperature result.

        :return: The value of the temperature sensor, in the format °C * 1_000
        :rtype: int
        """
        raw = self._read_raw()
        result = COMMAND_REGEX.findall(raw)[0]
        value = int(result)
        return value

    def _read_data(self) -> float:
        """Get the degrees celsius that the temperature sensor is reading.

        :return: Degrees celsius.
        :rtype: float
        """
        return self._read_temp() / 1_000
