from src.cicd.runners.language_runner import LanguageRunner


class LanguageRunnerFactory:
    _runners = {}

    @staticmethod
    def _init_runners():
        if not LanguageRunnerFactory._runners:
            for subclass in LanguageRunner.__subclasses__():
                instance = subclass()
                LanguageRunnerFactory._runners[instance.language] = instance

    @staticmethod
    def get(language: str) -> LanguageRunner:
        LanguageRunnerFactory._init_runners()
        if language not in LanguageRunnerFactory._runners:
            raise Exception(f"No builder found for language '{language}'")
        return LanguageRunnerFactory._runners[language]