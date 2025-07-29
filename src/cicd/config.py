import dagger
from dagger import field, Doc
from typing import Annotated

@dagger.object_type
class BaseConfig:
    component_type: Annotated[str, Doc("OpsLevel component type")]
    language: Annotated[str, Doc("Project language")]
    version: Annotated[str, Doc("Project Version")]
    source: Annotated[dagger.Directory, Doc("Source point to run the build")]

    @field
    def default_source(self) -> dagger.Directory:
        """Default source directory"""
        return dagger.dag.directory(".")