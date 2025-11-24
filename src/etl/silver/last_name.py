from collections.abc import Mapping
from typing import Any

import pandas as pd

from etl.core.base import ColumnMetadata, ColumnSpec


class LastName(ColumnSpec):
    meta = ColumnMetadata(
        name="last_name",
        title="Last Name",
        description="Last name canonicalized to title case.",
        good_examples=["Ng"],
        bad_examples=[None, ""],
        depends_on=(),
        input_fields=("lastname",),
        resources=(),
    )

    def transform(self, df: pd.DataFrame, resources: Mapping[str, Any] = {}) -> pd.Series:
        return (
            df["lastname"]
            .astype("string")
            .str.strip()
            .where(lambda s: s.str.len() > 0, other=None)
            .str.title()
        )
