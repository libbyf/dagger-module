import dagger
from dagger import dag, function, object_type

from .components.components_factory import ComponentFactory
from .config.base_config import BaseConfig


@object_type
class Cicd:

    @function
    def build(self, component_type: str, language: str, version: str, source: dagger.Directory) -> dagger.Container:
        """Returns a container built according to the base config parameters"""
        base_config = BaseConfig(component_type, language, version, source)

        component = ComponentFactory.get(base_config.component_type)
        return component.build(base_config)

    @function
    def test_1(self) -> dagger.Container:
        return dag.container().from_("alpine:latest").with_exec(["echo", "testtttttt_1"])

    @function
    def test(self, component_type: str, language: str, version: str, source: dagger.Directory) -> dagger.Container:
        """Returns a container that runs tests for the specified component type and language"""
        base_config = BaseConfig(component_type, language, version, source)

        component = ComponentFactory.get(base_config.component_type)
        runner = component.build(base_config)
        return component.test(runner, base_config)

    @function
    def container_echo(self, string_arg: str) -> dagger.Container:
        """Returns a container that echoes whatever string argument is provided"""
        return dag.container().from_("alpine:latest").with_exec(["echo", string_arg])

    # @function
    # async def grep_dir(self, directory_arg: dagger.Directory, pattern: str) -> str:
    #     """Returns lines that match a pattern in the files of the provided Directory"""
    #     return await (
    #         dag.container()
    #         .from_("alpine:latest")
    #         .with_mounted_directory("/mnt", directory_arg)
    #         .with_workdir("/mnt")
    #         .with_exec(["grep", "-R", pattern, "."])
    #         .stdout()
    #     )
