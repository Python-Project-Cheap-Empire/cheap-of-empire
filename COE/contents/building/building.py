from COE.contents.entity import Entity

"""
                  Entity
                    |
                    v
                Building
            /       |      \
      Military  Technology  Economy  (#pragma: no cover)
"""


# TODO : Add researches to require_researches and researches


class Building(Entity):
    def __init__(
        self,
        wood_required,
        stone_required,
        required_researches: set,
        required_age: int,
        required_building: set,
        construction_time: int,
        melee_armor: int,
        pierce_armor: int,
        **kwargs
    ):
        self.is_buildable = False
        self.wood_required = wood_required
        self.stone_required = stone_required
        self.required_researches = required_researches
        self.required_age = required_age
        self.required_building = required_building
        self.construction_time = construction_time
        self.melee_armor = melee_armor
        self.pierce_armor = pierce_armor
        self.construction_percent = 0
        super().__init__(**kwargs)

    def update_is_buildable(self):
        pass
