import dagger
from src.cicd.components.component import Component
from src.cicd.main import BaseConfig
from src.cicd.runners.language_runner_factory import LanguageRunnerFactory


class MicroServiceComponent(Component):

    @property
    def component_name(self):
        return "micro-service"

    def build(self, base_config: BaseConfig) -> dagger.Container:
        return (LanguageRunnerFactory.get(base_config.language)
                .build(base_config.version, base_config.source))

    def test(self, container: dagger.Container, base_config: BaseConfig) -> dagger.Container:
        return (LanguageRunnerFactory.get(base_config.language)
                .test(container, base_config.source))
