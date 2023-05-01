import importlib.resources as resources

__version__ = "1.0.0"

if __name__ == "__main__":
    raise RuntimeError("Don't run this module manually.")

_files = resources.files(__name__)
TEMPLATES = {
                child.name: child
                if child.name.endswith('tpl') else None
                for child in _files.iterdir()
            }

for key in tuple(TEMPLATES.keys()):
    if TEMPLATES[key] is None:
        TEMPLATES.pop(key)
