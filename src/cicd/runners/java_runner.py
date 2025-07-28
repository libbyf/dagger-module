import dagger
from dagger import dag

from src.cicd.runners.language_runner import LanguageRunner


class JavaRunner(LanguageRunner):

    @property
    def language(self):
        return "java"

    def build(self, version: str, source: dagger.Directory) -> dagger.Container:
        return (
            dag.container()
            .from_("eclipse-temurin:17-jdk")
            .with_directory("/app", source)
            .with_workdir("/app")
            .with_exec(["./gradlew", "build", "--no-daemon"])
        )

    def test(self, container: dagger.Container, source: dagger.Directory) -> dagger.Container:
        return container.with_exec(["./gradlew", "test", "--no-daemon"])
