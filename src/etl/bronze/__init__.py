import importlib
from collections.abc import Mapping
from typing import Any

import pandas as pd

from etl.core.ordering import topo_sort
from etl.core.registry import discover_columns
from etl.core.reporting import build_report
from etl.core.validation import validate_input_fields, validate_resources

_registry = discover_columns(pkg=importlib.import_module(__name__))


def run(
        df: pd.DataFrame,
        resources: Mapping[str, Any] = {},
    ) -> tuple[pd.DataFrame, dict[str, Any]]:
    validate_input_fields(df, _registry)
    validate_resources(resources, _registry)

    nodes = set(_registry.keys())
    edges: dict[str, set[str]] = {c: set() for c in nodes}
    for name, cls in _registry.items():
        for dep in cls.meta.depends_on:
            if dep not in nodes:
                raise KeyError(f"{name} depends on missing column '{dep}'")
            edges[dep].add(name)
    order = topo_sort(nodes, edges)

    out = df.copy()
    col_metrics = {}
    row_pass_flags = {}

    instances = {name: cls() for name, cls in _registry.items()}
    for name in order:
        spec = instances[name]
        series = spec.transform(out)
        out[spec.meta.name] = series
        row_flags = series.apply(lambda v: spec.qa_record(v)["passed"]).astype("boolean")
        row_pass_flags[name] = row_flags.fillna(False)
        col_metrics[name] = spec.qa_column(series)

    report = build_report(col_metrics, row_pass_flags)
    return out, report
