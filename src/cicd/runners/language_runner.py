from abc import ABC, abstractmethod
import dagger


class LanguageRunner(ABC):

    @property
    @abstractmethod
    def language(self) -> str:
        pass

    @abstractmethod
    def build(self, version: str, source: dagger.Directory) -> dagger.Container:
        pass

    @abstractmethod
    def test(self, container: dagger.Container, source: dagger.Directory) -> dagger.Container:
        pass