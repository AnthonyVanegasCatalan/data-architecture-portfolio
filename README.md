# Data Architecture Portfolio – E-Commerce Platform

## Author
**Anthony Joshua Vanegas**  
Data Architecture Engineer  
AWS | Python | Flyte | Delta Lake | Polars | SQL  

---

## Overview

This repository presents a production-grade **Data Architecture and Data Engineering solution** based on the designed for Magento API (Samsung.com) operating across multiple countries. And it also applies to all of our data sources listed below.

- Magento API
- Mirgor API
- SLC API
- SLC RPA
- COMPUMARKET API
- BONUS API
- STIENDA.UY API
- NICATEL RPA
- AIMNEXT RPA
- CLARO PR RPA
- GSCM RPA
- ALL FUTURE DATA SOURCES

The solution demonstrates how to:
- Design scalable data pipelines
- Orchestrate workflows using Flyte
- Implement Medallion Architecture on AWS
- Enforce data quality and governance
- Deliver analytics-ready data models

> ⚠️ This repository uses **mocked and anonymized examples** derived from real production workloads.  
> No sensitive data, credentials, or proprietary business logic is exposed.

---

## Business Context

The platform ingests **sales and inventory data** from multiple heterogeneous sources:
- REST APIs (JSON)
- XML feeds
- Historical datasets queried via Athena

Key challenges addressed:
- High data volume with frequent updates
- Multiple schemas and formats
- Idempotent ingestion and reprocessing
- Strong data quality requirements
- Multi-country, multi-business logic

---

## Architecture Summary

### Core Design Principles
- **Cloud-native** architecture on AWS
- **Medallion Architecture** (Bronze / Silver / Gold)
- **Idempotent ingestion** using hash-based merge keys
- **Separation of concerns** (ingestion, processing, governance)
- **Orchestration-first** design with Flyte

---

## High-Level Architecture

- **Ingestion Layer**
  - REST API (JSON)
  - XML feeds
  - Athena (historical reprocessing)

- **Storage Layer**
  - AWS S3
  - Delta Lake format
  - Partitioned by date and source

- **Processing Layer**
  - Polars for high-performance transformations
  - Business rule normalization
  - Dimensional enrichment

- **Orchestration**
  - Flyte tasks, workflows, and launch plans
  - Scheduled and conditional execution

- **Consumption Layer**
  - Dimensional tables
  - Fact tables
  - Analytics-ready datasets

---

## Medallion Architecture

### Bronze Layer (Raw)
- Raw data ingestion
- Schema preservation
- Delta Lake tables on S3
- Idempotent writes using merge keys
- Partitioned by `pulldate` and `source`

### Silver Layer (Validated & Enriched)
- Data type normalization
- Business rule application
- SKU standardization
- Currency and tax calculations
- Referential integrity checks
- Dimensional models
- Fact aggregation


### Gold Layer (Analytics Ready)
- Denormalized models
- Data Mart
- Optimized for BI tools (e.g. Power BI)

---

## Orchestration with Flyte

The platform uses **Flyte** as the orchestration engine to manage:
- Task dependencies
- Retry logic
- Resource allocation
- Conditional workflows
- Scheduled executions (cron-based)

### Key Features
- Modular task design
- Reusable workflows
- Support for historical reprocessing
- Failure policies and notifications

---

## Ingestion Strategy

### Sales Data
- Weekly extraction windows
- Parallel execution across countries
- Schema normalization at ingestion time
- Deduplication using hash-based merge keys

### Inventory Data
- XML parsing
- Dynamic schema handling
- Concurrent extraction
- Standardized output schema

---

## Data Quality & Governance

### Data Quality Gates
- Schema validation
- Null checks on critical fields
- Business rule validation
- Deduplication and consistency checks

### Governance Strategy
- Clear data layer ownership
- Controlled promotion from Bronze → Silver → Gold
- Audit-friendly transformations
- Reproducible historical loads

---

## Repository Structure

```text
data-architecture-portfolio/
│
├── README.md
│
├── architecture/
│   ├── architecture-overview.md
│   └── medallion-architecture.md
│
├── orchestration/
│   ├── workflows.py
│   └── launch_plan.py
│
├── ingestion/
│   ├── sales_api_ingestion.py
│   └── stock_xml_ingestion.py
│
├── bronze/
│   └── delta_writer.py
│
├── silver/
│   ├── sales_transformation.py
│   └── data_quality.py
│
├── governance/
│   └── data_governance.md
│
└── utils/
    └── config_placeholder.py
```

---

## Technology Stack

- Languages: Python, SQL
- Data Processing: Polars, Pandas
- Orchestration: Flyte
- Cloud: AWS (S3, Athena, Secrets Manager)
- Storage Format: Delta Lake
- Databases: MySQL / Analytical Warehouse
- Visualization: Power BI

---

## Key Takeaways

This portfolio demonstrates my ability to:
- Design and implement scalable data architectures
- Build production-ready ETL pipelines
- Apply data governance and quality controls
- Orchestrate complex workflows reliably
- Translate business requirements into robust data platforms

---

## Contact

Anthony Joshua Vanegas
a.vanegas@cheil.com
Data Architecture Engineer
