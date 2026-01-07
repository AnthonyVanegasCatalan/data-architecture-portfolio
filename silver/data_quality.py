"""
data_quality.py

Defines data quality validation rules used before promoting data
from Bronze to Silver and Silver to Gold layers.
"""

from typing import List
import polars as pl


# ===============================
# Schema Validation
# ===============================

def validate_required_columns(df: pl.DataFrame, required_columns: List[str]) -> None:
    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")


# ===============================
# Null Checks
# ===============================

def check_nulls(df: pl.DataFrame, critical_columns: List[str]) -> None:
    for col in critical_columns:
        if col in df.columns and df[col].null_count() > 0:
            raise ValueError(f"Null values found in critical column: {col}")


# ===============================
# Deduplication
# ===============================

def deduplicate(df: pl.DataFrame, subset: List[str]) -> pl.DataFrame:
    """
    Removes duplicate records based on a subset of columns.
    """
    return df.unique(subset=subset)


# ===============================
# Quality Gate
# ===============================

def silver_quality_gate(df: pl.DataFrame) -> pl.DataFrame:
    """
    Applies all quality rules before Silver layer persistence.
    """
    validate_required_columns(
        df,
        required_columns=["pulldate", "country"]
    )

    check_nulls(
        df,
        critical_columns=["pulldate", "country"]
    )

    return df
