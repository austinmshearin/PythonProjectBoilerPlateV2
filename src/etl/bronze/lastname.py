from collections.abc import Mapping
from typing import Any

import pandas as pd

from etl.core.base import ColumnMetadata, ColumnSpec


class Lastname(ColumnSpec):
    meta = ColumnMetadata(
        name="lastname",
        title="Last name (raw)",
        description="Raw last name as provided.",
        good_examples=["Ng", "O'Neil"],
        bad_examples=[None, ""],
        depends_on=(),
        input_fields=("firstname",),
        resources=(),
    )

    def transform(self, df: pd.DataFrame, resources: Mapping[str, Any] = {}) -> pd.Series:
        return df["lastname"].astype("string").str.strip().replace({"": None})
