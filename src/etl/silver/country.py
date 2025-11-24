from collections.abc import Mapping
from typing import Any

import pandas as pd

from etl.core.base import ColumnMetadata, ColumnSpec


class Country(ColumnSpec):
    meta = ColumnMetadata(
        name="country",
        title="Country",
        description="Country code",
        good_examples=["us", "united states"],
        bad_examples=[None, ""],
        depends_on=(),
        input_fields=("country",),
        resources=("country_lookup",),
    )

    def transform(self, df: pd.DataFrame, resources: Mapping[str, Any] = {}) -> pd.Series:
        assert resources is not None, "The country_lookup resource must be provided for the silver country transformer"
        lookup: Mapping[str, str] = resources["country_lookup"]
        s = df["country"].astype("string").str.strip().str.lower()
        out = s.map(lookup).fillna("UNK")
        return out
