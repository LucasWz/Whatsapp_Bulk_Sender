import yaml
from yaml.loader import SafeLoader


def load_yaml_config(path: str = "test.yml") -> dict:

    with open(path, mode="r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=SafeLoader)

    return data
