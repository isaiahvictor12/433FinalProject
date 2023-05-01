import importlib.resources as resources

__version__ = "1.0.0"

if __name__ == "__main__":
    raise RuntimeError("Don't run this module manually.")

_files = resources.files(__name__)
DIRECTORY = _files.joinpath('.')
