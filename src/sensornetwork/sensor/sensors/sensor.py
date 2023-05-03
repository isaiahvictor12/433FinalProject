from abc import ABC, abstractmethod
import threading
from time import sleep


class Sensor(ABC):

    def __init__(self, polling_time: float):
        self.polling_time = polling_time
        self._cached_reading = None
        self._collecting = True
        self._cache_lock = threading.Lock()
        self._thread = threading.Thread(target=self._thread_target)
        self._started = False

    @abstractmethod
    def _read_data(self) -> float:
        pass

    def _thread_target(self):
        self._started = True
        while self._collecting:
            with self._cache_lock:
                self._cached_reading = self._read_data()
            sleep(self.polling_time)

    def get_reading(self):
        if not self._started:
            self._thread.start()
        while self._cached_reading is None:
            pass
        return self._cached_reading

    def stop(self):
        self._collecting = False
        self._thread.join()

    def __del__(self):
        self.stop()