from collections.abc import Mapping
from typing import Any

import pandas as pd

from etl.core.base import ColumnMetadata, ColumnSpec


class FirstName(ColumnSpec):
    meta = ColumnMetadata(
        name="first_name",
        title="First Name",
        description="First name canonicalized to title case.",
        good_examples=["Alice"],
        bad_examples=[None, ""],
        depends_on=(),
        input_fields=("firstname",),
        resources=(),
    )

    def transform(self, df: pd.DataFrame, resources: Mapping[str, Any] = {}) -> pd.Series:
        return (
            df["firstname"]
            .astype("string")
            .str.strip()
            .where(lambda s: s.str.len() > 0, other=None)
            .str.title()
        )
