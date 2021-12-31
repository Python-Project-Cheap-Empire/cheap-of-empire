from .building import Building


class MilitaryBuilding(Building):  # pragma: no cover
    def __init__(self, **kwargs):
        self.pending_units = []
        super().__init__(**kwargs)
