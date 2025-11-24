import importlib
import inspect
import pkgutil
import types

from etl.core.base import ColumnSpec


def discover_columns(pkg: types.ModuleType) -> dict[str, type[ColumnSpec]]:
    registry = {}
    # Walk modules under the package
    for _, modname, ispkg in pkgutil.iter_modules(pkg.__path__, pkg.__name__ + "."):
        if ispkg:
            continue
        m = importlib.import_module(modname)
        for _, obj in vars(m).items():
            if inspect.isclass(obj) and issubclass(obj, ColumnSpec) and obj is not ColumnSpec:
                registry[obj.meta.name] = obj
    return dict(sorted(registry.items()))
