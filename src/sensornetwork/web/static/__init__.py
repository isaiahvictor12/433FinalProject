import importlib.resources as resources
from bottle import route, static_file


__version__ = "1.0.0"

if __name__ == "__main__":
    raise RuntimeError("Don't run this module manually.")

_files = resources.files(__name__)
STATIC_FILES = {
                    child.name: child
                    if not child.name.endswith('py') else None
                    for child in _files.iterdir()
                }

for key in tuple(STATIC_FILES.keys()):
    if STATIC_FILES[key] is None:
        STATIC_FILES.pop(key)


@route('/static/<path:path>')
def serve_static_files(path):
    stream = STATIC_FILES.get(path)
    if stream:
        return static_file(stream.read_bytes())
    else:
        return 404
