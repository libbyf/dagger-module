from abc import ABC, abstractmethod
from ..config.base_config import BaseConfig
import dagger



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