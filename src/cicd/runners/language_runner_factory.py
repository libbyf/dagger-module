from .language_runner import LanguageRunner


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
            available_languages = list(LanguageRunnerFactory._runners.keys())
            raise Exception(f"No runner found for language '{language}'. Available languages: {available_languages}")
        return LanguageRunnerFactory._runners[language]