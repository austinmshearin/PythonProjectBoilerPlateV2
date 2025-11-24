from collections.abc import Mapping
from typing import Any

import pandas as pd

from etl.core.base import ColumnMetadata, ColumnSpec


class FullName(ColumnSpec):
    meta = ColumnMetadata(
        name="full_name",
        title="Full Name",
        description="Concatenation of first_name and last_name.",
        good_examples=["Alice Ng"],
        bad_examples=[None, ""],
        depends_on=("first_name", "last_name"),
        input_fields=("firstname", "lastname"),
        resources=(),
    )

    def transform(self, df: pd.DataFrame, resources: Mapping[str, Any] = {}) -> pd.Series:
        fn = df["first_name"].astype("string")
        ln = df["last_name"].astype("string")
        # build full name safely with spaces; handle missing parts
        out = (fn.fillna("") + " " + ln.fillna("")).str.strip()
        return out.where(out.str.len() > 0, other=None)
