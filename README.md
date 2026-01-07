# Data Architecture Portfolio
Anthony Vanegas Data Architecture Portfolio

## Overview
This repository showcases my experience as a Data Architecture Engineer, focusing on the design and implementation of scalable, cloud-based data platforms on AWS.

The portfolio demonstrates:
- End-to-end ETL/ELT pipelines
- Medallion data architecture implementation
- Data quality and governance practices
- Workflow orchestration using Flyte
- AWS-native data services

> Note: All examples use mock data and simplified logic. No production or sensitive data is included.

---

## Architecture Overview

The platform is designed to ingest data from multiple heterogeneous sources, standardize it, and expose curated datasets for analytics and reporting.

**Data Sources**
- APIs
- CSV / Excel files
- HTML data sources

**Core Components**
- Ingestion: Python-based pipelines
- Storage: AWS S3 (Bronze, Silver, Gold layers)
- Processing: AWS Glue & Lambda
- Governance: AWS Lake Formation
- Query Engine: AWS Athena
- Orchestration: Flyte
- Visualization: Power BI

Architecture diagrams are available in the `/architecture` folder.

---

## Medallion Architecture

The data platform follows the Medallion Architecture pattern:

- **Bronze**: Raw ingested data
- **Silver**: Cleaned and standardized datasets
- **Gold**: Curated, analytics-ready data models

This approach ensures data quality, scalability, and clear data ownership.

---

## ETL / ELT Pipelines

Reusable ingestion and transformation logic is implemented using Python, following modular and extensible design principles.

Key features:
- Reusable base ingestion classes
- Centralized error handling
- Schema validation
- Data quality checks before promotion to Silver and Gold layers

---

## Orchestration

All pipelines are orchestrated using Flyte, enabling:
- Dependency management
- Retry logic
- Monitoring and observability
- Scalable execution

---

## Governance & Data Quality

Governance is enforced using:
- AWS Lake Formation for access control
- Schema validation and quality checks
- Controlled promotion between data layers

---

## Technology Stack

- **Languages**: Python, SQL
- **Cloud**: AWS (S3, Glue, Athena, Lambda, Lake Formation)
- **Orchestration**: Flyte
- **Visualization**: Power BI
- **Version Control**: Git

---

## Contact

Anthony Joshua Vanegas  
Data Architecture Engineer
