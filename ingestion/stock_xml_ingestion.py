"""
stock_xml_ingestion.py

Ingests inventory data from XML feeds.
Handles schema variability and normalization.
"""

import requests
import xml.etree.ElementTree as ET
from typing import List, Dict


class StockXMLIngestion:
    def __init__(self, endpoints: List[Dict[str, str]]):
        self.endpoints = endpoints

    def extract(self) -> List[dict]:
        """
        Extracts product stock data from multiple XML endpoints.
        """
        results = []

        for ep in self.endpoints:
            country = ep.get("country")
            url = ep.get("source")

            try:
                response = requests.get(url, timeout=60)
                response.raise_for_status()

                xml_content = response.text.lstrip()
                if xml_content.startswith("<?xml"):
                    xml_content = xml_content.split("?>", 1)[1]

                root = ET.fromstring(xml_content)
                products = root.find(".//products")

                if products is None:
                    continue

                for product in products.findall("./product"):
                    row = {"country": country}

                    for field in product:
                        if field.text:
                            row[field.tag] = field.text

                    results.append(row)

            except Exception as exc:
                print(f"[STOCK INGESTION ERROR] {country}: {exc}")

        return results
