import dagger
from dagger import dag, function, object_type, field, Doc
from typing import Annotated

@object_type
class BaseConfig:
    component_type: Annotated[str, Doc("OpsLevel component type")] = field()
    language: Annotated[str, Doc("Project language")] = field()
    version: Annotated[str, Doc("Project Version")] = field()
    source =  Annotated[dagger.Directory, Doc("Source point to run the commands")] = field(default=dagger.Directory("."))