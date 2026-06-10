from pathlib import Path

import yaml


def read_config(filepath: Path) -> dict:
    """
    Read in a config yaml to a dictionary.

    Args:
        filepath (Path): path to read from

    Returns:
        dict: loaded config yaml as dictionary
    """
    with open(filepath, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    return config


def write_config(config: dict, filepath: Path):
    """
    Write out a config dictionary to a yaml file for audit.

    Args:
        config (dict): config dictionary to save
        filepath (Path): path to save to
    """

    def yaml_dump_path(dumper, obj):
        return dumper.represent_scalar("tag:yaml.org,2002:str", str(obj))

    yaml.add_multi_representer(Path, yaml_dump_path)

    with open(filepath, "w", encoding="utf-8") as f:
        yaml.dump(config, f, default_flow_style=False)
