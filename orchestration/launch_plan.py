"""
launch_plan.py

Defines scheduled execution plans for Flyte workflows.
Demonstrates production-style orchestration and automation.
"""

from flytekit import LaunchPlan, CronSchedule, Email, WorkflowExecutionPhase
from datetime import datetime
from orchestration.workflows import ecommerce_pipeline


# ===============================
# Daily Scheduled Execution
# ===============================

daily_ecommerce_pipeline = LaunchPlan.get_or_create(
    name="daily-ecommerce-data-pipeline",
    workflow=ecommerce_pipeline,
    schedule=CronSchedule(
        schedule="45 13 * * *",  # Daily at 08:45 UTC-5
        kickoff_time_input_arg="kickoff_time",
    ),
    fixed_inputs={
        "is_historical": False
    },
    notifications=[
        Email(
            phases=[WorkflowExecutionPhase.SUCCEEDED],
            recipients_email=["data-team@example.com"],
        )
    ],
)
