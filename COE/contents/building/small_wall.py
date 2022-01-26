from .building import Building
from .granary import Granary


class SmallWall(Building):
    def __init__(self, position: tuple):
        super().__init__(
            name="Small Wall",
            hp=100,
            positions=position,
            width=1,
            height=1,
            line_of_sight=1,
            required_building={Granary.__class__.__name__},
            required_age=2,
            required_researches={},  # Need research small wall
            researches={},
            wood_required=20,
            time_construction=10,
        )
