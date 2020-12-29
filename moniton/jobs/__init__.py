import importlib
import pkgutil

import inspect


def _get_classes(module):
    cls = []
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            cls.extend(obj.__subclasses__())
    return cls

def get_jobs():
    module = importlib.import_module('.', __package__)
    module_path = module.__path__[0]
    for (module_loader, name, ispkg) in pkgutil.iter_modules([module_path]):
        module = importlib.import_module('.' + name, __package__)
        for cls in _get_classes(module):
            yield cls
