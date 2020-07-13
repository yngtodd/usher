import toml

from pathlib import Path


def get_project_root() -> Path:
    r"""Returns project root folder"""
    return Path(__file__).parent.parent


def get_project_config() -> Path:
    r"""Get the path the project config file"""
    return get_project_root().joinpath('.projectusher.toml')


def get_data_root() -> Path:
    r"""Get root path to the data from the project config"""
    config = toml.load(get_project_config())
    data = Path(config['dat']['path'])
    return get_project_root().joinpath(data)
