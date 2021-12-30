from .building import Building


# Resources will be modified later due to enumeration of Resources
class StorageBuilding(Building):
    def __init__(
        self, resources, max_held: int, **kwargs
    ):  # Resources: set of Resources
        self.resources = resources
        self.max_held = max_held
        super().__init__(**kwargs)
