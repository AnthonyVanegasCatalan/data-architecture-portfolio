"""
workflows.py

Defines Flyte tasks and workflows orchestrating
the end-to-end data pipeline.
"""

from datetime import datetime
from flytekit import task, workflow

from ingestion.sales_api_ingestion import SalesAPIIngestion
from bronze.delta_writer import write_bronze_delta
from silver.sales_transformation import transform_sales


@task
def extract_sales_task() -> list:
    endpoints = [
        {"country": "US", "url": "https://api.example.com/sales"},
        {"country": "KR", "url": "https://api.example.com/sales"},
    ]

    ingestion = SalesAPIIngestion(endpoints=endpoints)
    return ingestion.extract()


@task
def write_bronze_task(raw_sales: list) -> None:
    write_bronze_delta(raw_sales, target="sales")


@task
def transform_sales_task(raw_sales: list) -> None:
    transform_sales(raw_sales)


@workflow
def ecommerce_pipeline(
    kickoff_time: datetime,
    is_historical: bool = False,
):
    raw_sales = extract_sales_task()
    write_bronze_task(raw_sales)
    transform_sales_task(raw_sales)
