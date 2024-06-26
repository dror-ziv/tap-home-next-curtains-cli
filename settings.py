import json
import yaml
import os
from enum import Enum

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class TapHomeClientSettings(BaseSettings):
    server_url: str = Field(env="SERVER_URL")
    username: str = Field(env="USERNAME")
    hashed_password: str = Field(env="HASHED_PASSWORD")
    my_curtains_names: list[str] = []


def load_from_config() -> TapHomeClientSettings:
    script_dir = os.path.dirname(
        os.path.abspath(__file__)
    )  # Get the directory of the current script
    config_file_path = os.path.join(script_dir, "config.yaml")

    with open(config_file_path, "r") as config_file:
        config_data = yaml.safe_load(config_file)

    return TapHomeClientSettings(
        server_url=config_data["server_url"],
        username=config_data["username"],
        hashed_password=config_data["hashed_password"],
        my_curtains_names=config_data["my_curtains_names"],
    )


class Curtain(BaseModel):
    id: int
    name: str


def load_my_curtains_from_cache() -> list[Curtain]:
    script_dir = os.path.dirname(
        os.path.abspath(__file__)
    )  # Get the directory of the current script
    config_file_path = os.path.join(script_dir, "curtains_cache.json")
    with open(config_file_path, "r") as config_file:
        config_data = json.load(config_file)
    return [Curtain(name=key, id=value) for key, value in config_data.items()]


def set_my_curtains_cache(curtains: list[Curtain]) -> None:
    script_dir = os.path.dirname(
        os.path.abspath(__file__)
    )  # Get the directory of the current script
    config_file_path = os.path.join(script_dir, "curtains_cache.json")

    config_data = {curtain.name: curtain.id for curtain in curtains}

    # Write the data to the JSON file
    with open(config_file_path, "w") as config_file:
        json.dump(config_data, config_file, indent=4)


def is_curtain_names_in_curtains(curtain_names: list[str], cache_curtains: list[Curtain])-> bool:
    cached_names = [curtain.name for curtain in cache_curtains]
    for curtain in curtain_names:
        if curtain not in cached_names:
            return False
    return True


def query_cache_curtains(curtain_names: list[str])-> list[Curtain]:
    cache = load_my_curtains_from_cache()
    result = []
    for target_curtain in curtain_names:
        for cached_curtain in cache:
            if target_curtain == cached_curtain.name:
                result.append(cached_curtain)
    return result

class CurtainLevel(Enum):
    UP = 92
    DOWN = 6
