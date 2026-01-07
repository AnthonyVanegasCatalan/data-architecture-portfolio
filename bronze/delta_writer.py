def write_bronze_delta(df, target: str):
    """
    Writes raw data to S3 using Delta Lake.
    - Partitioned by pulldate and source
    - Idempotent writes using merge keys
    """
    pass
