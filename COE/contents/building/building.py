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
        **kwargs
    ):
        self.is_buildable = False
        self.wood_required = wood_required
        self.stone_required = (stone_required,)
        self.required_researches = required_researches
        self.required_age = required_age
        self.required_building = required_building
        super().__init__(**kwargs)

    def update_is_buildable(self):
        pass
