from .building import Building


class MilitaryBuilding(Building):  # pragma: no cover
    def __init__(self, unit_type: str = "", pending_units: list = []):
        super().__init__(self)
        self.unit_type = unit_type
        self.pending_units = pending_units
