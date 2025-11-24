from collections.abc import Mapping
from typing import Any

import pandas as pd

from etl.core.base import ColumnMetadata, ColumnSpec


class Country(ColumnSpec):
    meta = ColumnMetadata(
        name="country",
        title="Country",
        description="Raw country text field",
        good_examples=["us", "united states"],
        bad_examples=[None, ""],
        depends_on=(),
        input_fields=("country",),
        resources=(),
    )

    def transform(self, df: pd.DataFrame, resources: Mapping[str, Any] = {}) -> pd.Series:
        return df["country"].astype("string").str.strip().str.lower().replace({"": None})
