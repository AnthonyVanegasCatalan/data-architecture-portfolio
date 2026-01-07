"""
delta_writer.py

Handles idempotent writes to the Bronze layer
using Delta Lake on AWS S3.
"""

from typing import List
import polars as pl
import hashlib


def _generate_hash_key(row: dict, keys: List[str]) -> str:
    concat = "|".join(str(row.get(k, "")) for k in keys)
    return hashlib.md5(concat.encode()).hexdigest()


def write_bronze_delta(data: List[dict], target: str) -> None:
    """
    Writes raw data to Bronze Delta tables.
    - Hash-based merge key
    - Partitioned by pulldate
    """

    if not data:
        print("[BRONZE] No data to write")
        return

    df = pl.DataFrame(data)

    if "merge_key" not in df.columns:
        df = df.with_columns(
            pl.struct(df.columns)
            .map_elements(lambda r: _generate_hash_key(r, df.columns))
            .alias("merge_key")
        )

    # Placeholder for Delta Lake write
    print(
        f"[BRONZE WRITE] Target={target} | "
        f"Records={df.height} | "
        f"Partitions=pulldate"
    )

    # In production:
    # df.write_delta(
    #     f"s3://bronze-bucket/{target}",
    #     mode="merge",
    #     merge_on="merge_key"
    # )
