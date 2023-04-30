import importlib.resources as resources

__version__ = "1.0.0"
DATABASE = "sensornetwork"

if __name__ == "__main__":
    raise RuntimeError("Don't run this module manually.")

_files = resources.files(__name__)
INIT_SCRIPT = _files.joinpath("init.sql")
DROP_SCRIPT = _files.joinpath("drop.sql")
