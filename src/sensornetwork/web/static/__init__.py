import importlib.resources as resources

__version__ = "1.0.0"

if __name__ == "__main__":
    raise RuntimeError("Don't run this module manually.")

_files = resources.files(__name__)
STATIC_FILES = {
                    child.name: child
                    if not (child.name.endswith('.py') or child.name[0] == '.' or child.name[0] == '_') else None
                    for child in _files.iterdir()
                }

for key in tuple(STATIC_FILES.keys()):
    if STATIC_FILES[key] is None:
        STATIC_FILES.pop(key)
