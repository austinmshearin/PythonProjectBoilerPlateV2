from typing import Any

import pandas as pd


def build_report(
    per_col_col_metrics: dict[str, dict[str, float | int]],
    per_col_row_flags: dict[str, pd.Series],
) -> dict[str, Any]:
    joined_flags = None
    for s in per_col_row_flags.values():
        joined_flags = s if joined_flags is None else (joined_flags & s)
    return {
        "column_metrics": per_col_col_metrics,
        "record_passed": None if joined_flags is None else joined_flags,
        "dataset_pass_rate": None if joined_flags is None else float(joined_flags.mean()),
    }
