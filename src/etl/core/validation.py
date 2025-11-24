from collections.abc import Mapping
from typing import Any

import pandas as pd

from etl.core.base import ColumnSpec


def validate_input_fields(df: pd.DataFrame, registry: dict[str, type[ColumnSpec]]) -> None:
    """Ensure all declared input_fields exist in dataframe columns."""
    required = set()
    by_field: dict[str, list[str]] = {}

    for name, cls in registry.items():
        for f in cls.meta.input_fields:
            required.add(f)
            by_field.setdefault(f, []).append(name)

    missing = [c for c in sorted(required) if c not in df.columns]
    if missing:
        details = "; ".join(f"{c} (needed by: {', '.join(by_field[c])})" for c in missing)
        raise KeyError(f"Missing required input fields in dataframe: {details}")

def validate_resources(resources: Mapping[str, Any], registry: dict[str, type[ColumnSpec]]) -> None:
    required: set[str] = set()
    by_key: dict[str, list[str]] = {}
    for name, cls in registry.items():
        for r in cls.meta.resources:
            required.add(r)
            by_key.setdefault(r, []).append(name)
    missing = [k for k in sorted(required) if k not in resources]
    if missing:
        details = "; ".join(f"{k} (needed by: {', '.join(by_key[k])})" for k in missing)
        raise KeyError(f"Missing required resources: {details}")
