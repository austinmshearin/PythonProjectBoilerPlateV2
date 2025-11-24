from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any, TypedDict

import pandas as pd


class RecordQAResult(TypedDict, total=False):
    passed: bool
    reasons: list[str]
    metrics: dict[str, float | int | bool]

@dataclass(frozen=True)
class ColumnMetadata:
    name: str
    title: str
    description: str
    good_examples: Sequence[object]
    bad_examples: Sequence[object]
    depends_on: Sequence[str] = ()
    input_fields: Sequence[str] = ()
    resources: Sequence[str] = ()

class ColumnSpec(ABC):
    meta: ColumnMetadata

    @abstractmethod
    def transform(
        self,
        df: pd.DataFrame,
        resources: Mapping[str, Any] = {},
    ) -> pd.Series:
        """Compute your output column using df that contains required input_fields."""

    def qa_record(self, value: Any) -> RecordQAResult:
        return {"passed": value is not None, "reasons": [] if value is not None else ["null"], "metrics": {}}

    def qa_column(self, series: pd.Series) -> dict[str, float | int]:
        s = series.dropna()
        return {
            "count": int(series.size),
            "null_pct": float(series.isna().mean()),
            "distinct": int(s.nunique()),
        }
