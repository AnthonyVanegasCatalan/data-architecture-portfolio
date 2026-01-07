```mermaid
flowchart LR
    A[External Data Sources]
    A1[REST APIs<br/>JSON]
    A2[XML Feeds]
    A3[Athena<br/>Historical Data]

    B[Flyte Orchestration]

    C[Ingestion Layer<br/>Python + Polars]
    D[Bronze Layer<br/>S3 + Delta Lake]

    E[Silver Layer<br/>Transformations & QA]
    F[Gold Layer<br/>Dimensional Models]

    G[Analytics<br/>Power BI]

    A1 --> B
    A2 --> B
    A3 --> B

    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
