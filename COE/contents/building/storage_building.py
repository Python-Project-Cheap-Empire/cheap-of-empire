from .building import Building


# Ressource will be modified later due to enumeration of Ressource
class StorageBuilding(Building):
    def __init__(self, ressources, max_held: int):  # ressources: set of Ressource
        super().__init__(self)
        self.ressources = ressources
        self.max_held = max_held
