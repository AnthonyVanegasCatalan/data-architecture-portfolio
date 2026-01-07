"""
sales_api_ingestion.py

Ingests sales data from REST APIs (JSON).
Supports multiple countries, parallel extraction windows,
and schema normalization suitable for Bronze layer storage.
"""

import requests
from datetime import date, timedelta
from typing import List, Dict


class SalesAPIIngestion:
    def __init__(self, endpoints: List[Dict[str, str]], weeks_back: int = 12):
        self.endpoints = endpoints
        self.weeks_back = weeks_back

    def _date_windows(self) -> List[Dict[str, date]]:
        today = date.today()
        return [
            {
                "start": today - timedelta(weeks=i + 1),
                "end": today - timedelta(weeks=i),
            }
            for i in range(self.weeks_back)
        ]

    def extract(self) -> List[dict]:
        """
        Extracts sales data using rolling weekly windows.
        """
        results = []

        for ep in self.endpoints:
            country = ep["country"]
            url = ep["url"]

            for window in self._date_windows():
                params = {
                    "start_date": window["start"].isoformat(),
                    "end_date": window["end"].isoformat(),
                }

                try:
                    response = requests.get(url, params=params, timeout=60)
                    response.raise_for_status()
                    payload = response.json()

                    for row in payload.get("data", []):
                        row["country"] = country
                        row["pulldate"] = window["end"].isoformat()
                        results.append(row)

                except Exception as exc:
                    print(f"[SALES INGESTION ERROR] {country} {params}: {exc}")

        return results
