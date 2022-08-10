import csv
from typing import List, Dict


def save_data(rows: List[Dict[str, str]], path: str = "test.csv") -> None:
    with open(path, "w", encoding="UTF8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
