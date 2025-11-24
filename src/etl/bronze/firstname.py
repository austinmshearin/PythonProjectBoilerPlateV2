from collections.abc import Mapping
from typing import Any

import pandas as pd

from etl.core.base import ColumnMetadata, ColumnSpec


class Firstname(ColumnSpec):
    meta = ColumnMetadata(
        name="firstname",
        title="First name (raw)",
        description="Raw first name as provided.",
        good_examples=["alice", "Bob"],
        bad_examples=[None, ""],
        depends_on=(),
        input_fields=("firstname",),
        resources=(),
    )

    def transform(self, df: pd.DataFrame, resources: Mapping[str, Any] = {}) -> pd.Series:
        return df["firstname"].astype("string").str.strip().replace({"": None})
