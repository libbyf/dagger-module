import dagger
from dataclasses import dataclass


@dataclass
class BaseConfig:
    component_type: str
    language: str
    version: str
    source: dagger.Directory = None