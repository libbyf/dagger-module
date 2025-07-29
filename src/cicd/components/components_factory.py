from .component import Component


class ComponentFactory:
    _components = {}

    @staticmethod
    def _init_components():
        if not ComponentFactory._components:
            subclasses = Component.__subclasses__()
            print(f"Found component subclasses: {subclasses}")
            for subclass in subclasses:
                instance = subclass()
                ComponentFactory._components[instance.component_name] = instance
            print(f"Registered components: {list(ComponentFactory._components.keys())}")
        else:
            print("components already initialized")

    @staticmethod
    def get(component_type: str) -> Component:
        ComponentFactory._init_components()
        if component_type not in ComponentFactory._components:
            available_types = list(ComponentFactory._components.keys())
            raise Exception(f"No component found for type '{component_type}'. Available types: {available_types}")
        return ComponentFactory._components[component_type]