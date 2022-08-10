from pathlib import Path
from typing import Dict, List, Optional

import pandas as pd


class InputDataError(Exception):
    pass


def validate_contacts(data: List[Dict[str, str]]) -> Optional[List[Dict[str, str]]]:
    """
    Convert to dataframe and validate : column headers and
    'WhatsApp Number(with country code)' column pattern as french phone numbers
    with no missing values nor duplicated values.

    Args:
        data (List[Dict[str, str]]): Contacts data parsed from csv file.

    Raises:
        InputDataError: Custom Error to handle input data validation.

    Returns:
        Optional[List[Dict[str, str]]]: Unchanged input data or raises error.
    """

    columns = {
        "WhatsApp Number(with country code)",
        "Saved Name",
        "Sent",
    }

    df = pd.DataFrame(data)

    # validate columns name
    if not set(columns).issubset(df.columns):
        raise InputDataError(
            f"""'contacts.csv' column header must be '{"', '".join(columns)}'."""
        )

    # validate french number pattern with indicativ prefix
    pattern = "^(\+(33|590|594|596|269|687|689|262|508|681))[0-9]{9}$"
    phone_numbers = df["WhatsApp Number(with country code)"]

    is_french = phone_numbers.str.fullmatch(pattern)
    if ~is_french.all():
        phone_numbers = ", ".join(list(phone_numbers[~is_french].values))
        raise InputDataError(
            f"""Some phone numbers doesn't respect pattern : {phone_numbers}"""
        )

    # validate NaN
    if phone_numbers.isna().any():
        raise InputDataError(f"""Some phone numbers are missing.""")

    # validate duplicates
    if phone_numbers.duplicated().any():
        raise InputDataError(
            f"""Some phone numbers are duplicated : {', '.join(list(set(phone_numbers[phone_numbers.duplicated()].values)))}"""
        )

    return data


def validate_files(folder: str) -> Optional[str]:

    assert Path(folder).exists(), f"Folder '{folder}' doesn't exists."

    template_files = {
        "message": [".txt"],
        "config": [".yml"],
        "contacts": [".csv"],
        "picture": [".png", ".jpg", ".gif"],
    }

    files_stems = [(path.stem, path.suffix) for path in Path(folder).glob("*.*")]

    for stem, suffix in files_stems:
        if stem in template_files:
            if suffix in template_files[stem]:
                template_files.pop(stem)

    if len(template_files) > 0:
        template_files = " - ".join(
            [
                f"""'{k}' -> '{"', '".join(v)}'""" + "\n"
                for k, v in template_files.items()
            ]
        )
        raise FileNotFoundError(
            f"Those files are mandatory in {folder}:\n - {template_files}"
        )

    return folder


def validate_message(s: str) -> Optional[str]:

    if len(s.replace("*", "")) > 700:
        raise InputDataError("Message lenght is greater than 700 characters.")

    return s


def validate_config(data) -> Optional[Dict[str, str]]:
    parameters = ["chrome_profile", "message_path", "contacts_path", "attachment_path"]

    for parameter in parameters:
        if parameter not in data:
            raise InputDataError(
                f"Please add {parameter} parameter to the file 'config.yml'."
            )
    return data
