import json
import yaml
import os
from enum import Enum

from pydantic import BaseModel


class TapHomeClientSettings(BaseModel):
    server_url: str
    username: str
    hashed_password: str
    my_curtains_names: list[str]


def load_from_config() -> TapHomeClientSettings:
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    config_file_path = os.path.join(script_dir, 'config.yaml')

    with open(config_file_path, 'r') as config_file:
        config_data = yaml.safe_load(config_file)

    return TapHomeClientSettings(
        server_url=config_data['server_url'],
        username=config_data['username'],
        hashed_password=config_data['hashed_password'],
        my_curtains_names=config_data['my_curtains_names']
    )


class Curtain(BaseModel):
    id: int
    name: str


def load_my_curtains_from_cache() -> list[Curtain]:
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    config_file_path = os.path.join(script_dir, 'curtains_cache.json')
    with open(config_file_path, 'r') as config_file:
        config_data = json.load(config_file)
    return [Curtain(name=key, id=value) for key, value in config_data.items()]


def set_my_curtains_cache(curtains: list[Curtain]) -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
    config_file_path = os.path.join(script_dir, 'curtains_cache.json')

    config_data = {curtain.name: curtain.id for curtain in curtains}

    # Write the data to the JSON file
    with open(config_file_path, 'w') as config_file:
        json.dump(config_data, config_file, indent=4)


class CurtainLevel(Enum):
    UP = 92
    DOWN = 6
