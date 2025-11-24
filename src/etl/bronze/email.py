import re
from collections.abc import Mapping
from typing import Any

import pandas as pd

from etl.core.base import ColumnMetadata, ColumnSpec, RecordQAResult

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

class Email(ColumnSpec):
    meta = ColumnMetadata(
        name="email",
        title="Email (raw)",
        description="Raw email, lowercased & trimmed.",
        good_examples=["a@b.com"],
        bad_examples=["not_an_email"],
        depends_on=(),
        input_fields=("email",),
        resources=(),
    )

    def transform(self, df: pd.DataFrame, resources: Mapping[str, Any] = {}) -> pd.Series:
        return df["email"].astype("string").str.strip().str.lower().replace({"": None})

    def qa_record(self, value: Any) -> RecordQAResult:
        ok = value is not None and isinstance(value, str) and bool(EMAIL_RE.match(value))
        return {
            "passed": ok,
            "reasons": [] if ok else ["invalid_email_format"],
            "metrics": {"len": len(value) if isinstance(value, str) else 0},
        }
