"""
sales_transformation.py

Applies business logic, data quality rules,
and prepares data for Silver and Gold layers.
"""

import polars as pl
from typing import List
from silver.data_quality import silver_quality_gate


def transform_sales(raw_data: List[dict]) -> None:
    """
    Transforms raw sales data:
    - Type casting
    - Status normalization
    - Business rule application
    """

    if not raw_data:
        print("[SILVER] No data to transform")
        return

    df = pl.DataFrame(raw_data)

    # Basic normalization
    df = df.with_columns([
        pl.col("country").str.to_uppercase(),
        pl.col("pulldate").str.strptime(pl.Date, strict=False),
    ])

    # Example business rule
    if "status" in df.columns:
        df = df.with_columns(
            pl.when(pl.col("status") == "completed")
            .then("SUCCESS")
            .otherwise("OTHER")
            .alias("order_status")
        )

    # Apply quality gate
    df = silver_quality_gate(df)

    print(
        f"[SILVER TRANSFORM] Records={df.height} | "
        f"Columns={len(df.columns)}"
    )

    # In production:
    # df.write_parquet("s3://silver-bucket/sales/")
