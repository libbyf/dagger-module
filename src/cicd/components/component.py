from abc import ABC, abstractmethod
import dagger



class Component(ABC):

    @property
    @abstractmethod
    def component_name(self) -> str:
        """Unique name for this service type"""
        pass

    @abstractmethod
    def build(self, base_config) -> dagger.Container:
        pass

    @abstractmethod
    def test(self, container: dagger.Container, base_config) -> dagger.Container:
        pass