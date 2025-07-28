from .component import Component


class ComponentFactory:
    _components = {}

    @staticmethod
    def _init_components():
        if not ComponentFactory._components:
            for subclass in Component.__subclasses__():
                instance = subclass()
                ComponentFactory._components[instance.component_name] = instance

    @staticmethod
    def get(component_type: str) -> Component:
        if ComponentFactory._components == {}:
           ComponentFactory._init_components()
        if component_type not in ComponentFactory._components:
            raise Exception(f"No matching component found for type '{component_type}'")
        return ComponentFactory._components[component_type]