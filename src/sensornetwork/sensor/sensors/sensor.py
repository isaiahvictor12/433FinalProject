from abc import ABC, abstractmethod
import threading
from time import sleep


class Sensor(ABC):

    def __init__(self, polling_time: float):
        self.polling_time = polling_time
        self._cached_reading = None
        self._thread = threading.Thread(target=self._thread_target)
        self._thread.start()
        self._collecting = True
        self._cache_lock = threading.Lock()

    @abstractmethod
    def _read_data(self) -> float:
        pass

    def _thread_target(self):
        while self._collecting:
            with self._cache_lock:
                self._cached_reading = self._read_data()
            sleep(self.polling_time)

    def get_reading(self):
        while self._cached_reading is None:
            if not self._thread.is_alive():
                self._thread.start()
        return self._cached_reading
