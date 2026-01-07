@workflow
def magento_pipeline(kickoff_time: datetime, is_historical: bool = False):
    raw_sales = extract_sales(kickoff_time)
    write_bronze(raw_sales, target="sales")

    transformed = transform_sales(raw_sales)
    load_dimensions(transformed)
    load_facts(transformed)
