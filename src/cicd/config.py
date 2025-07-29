import dagger
from dagger import field, Doc, object_type
from typing import Annotated

@object_type
class BaseConfig:
    component_type: Annotated[str, Doc("OpsLevel component type")] = field()
    language: Annotated[str, Doc("Project language")] = field()
    version: Annotated[str, Doc("Project Version")] = field()
    source: Annotated[dagger.Directory, Doc("Source point to run the build")] = field()