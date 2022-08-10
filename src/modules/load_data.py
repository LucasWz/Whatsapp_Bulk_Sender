import csv
from typing import Dict, List


def load_contacts(path: str) -> List[Dict[str, str]]:

    with open(path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        contacts = [row for row in csv_reader]

    return contacts


def load_message(path: str) -> str:

    with open(path, mode="r", encoding="utf-8") as f:
        message = "".join(f.readlines())

    return message
