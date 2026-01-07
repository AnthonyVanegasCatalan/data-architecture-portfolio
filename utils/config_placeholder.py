"""
config_placeholder.py

This module represents environment configuration and secrets management
used in production systems.

⚠️ NOTE:
- This file contains ONLY placeholders.
- In production, secrets are retrieved securely from services such as
  AWS Secrets Manager or environment variables.
- No credentials are stored in source control.
"""

from dataclasses import dataclass
from typing import Optional


# ===============================
# Environment Configuration
# ===============================

@dataclass
class AWSConfig:
    region: str = "us-east-1"
    bronze_bucket: str = "example-bronze-bucket"
    bronze_base_path: str = "datalake/bronze"


@dataclass
class DatabaseConfig:
    host: str = "db-host-placeholder"
    user: str = "db-user-placeholder"
    password: str = "********"
    database: str = "example_database"


@dataclass
class WarehouseConfig:
    host: str = "warehouse-host-placeholder"
    user: str = "warehouse-user-placeholder"
    password: str = "********"
    database: str = "example_warehouse"


# ===============================
# Runtime Settings
# ===============================

@dataclass
class PipelineConfig:
    datasource_id: int = 0
    default_weeks_back: int = 12
    enable_historical_load: bool = False


# ===============================
# Configuration Factory
# ===============================

class ConfigFactory:
    """
    Factory pattern to provide configuration objects.

    In real environments, values would be injected from:
    - AWS Secrets Manager
    - Environment variables
    - CI/CD pipelines
    """

    @staticmethod
    def aws() -> AWSConfig:
        return AWSConfig()

    @staticmethod
    def database() -> DatabaseConfig:
        return DatabaseConfig()

    @staticmethod
    def warehouse() -> WarehouseConfig:
        return WarehouseConfig()

    @staticmethod
    def pipeline() -> PipelineConfig:
        return PipelineConfig()
