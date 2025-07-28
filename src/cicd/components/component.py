from abc import ABC, abstractmethod
import dagger

from ..main import BaseConfig


class Component(ABC):

    @property
    @abstractmethod
    def component_name(self) -> str:
        """Unique name for this service type"""
        pass

    @abstractmethod
    def build(self, base_config: BaseConfig) -> dagger.Container:
        pass

    @abstractmethod
    def test(self, container: dagger.Container, base_config: BaseConfig) -> dagger.Container:
        pass