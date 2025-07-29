import dagger
from dagger import dag

from .language_runner import LanguageRunner


class PythonRunner(LanguageRunner):

    @property
    def language(self):
        return "python"

    def build(self, version: str, source: dagger.Directory) -> dagger.Container:
        return (
            dag.container()
            .from_(f"python:{version}")
            .with_directory("/app", source)
            .with_workdir("/app")
            .with_exec(["pip", "install", "-r", "requirements.txt"])
        )

    def test(self, container: dagger.Container, source: dagger.Directory) -> dagger.Container:
        return (container
                .with_env_variable("PYTHONPATH", "/app")
                .with_exec(["pytest", "-m", "test"]))