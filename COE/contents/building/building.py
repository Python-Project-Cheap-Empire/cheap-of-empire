from COE.contents.entity import Entity

"""
                  Entity
                    |
                    v
                Building
            /       |      \
      Military  Technology  Economy  (#pragma: no cover)
"""


class Building(Entity):
    def __init__(
        self,
        is_buildable: bool = False,
        required_researches: set = {},
        required_age: int = None,
        required_building: set = {},
        **kwargs
    ):
        self.is_buildable = is_buildable
        self.required_researches = required_researches
        self.required_age = required_age
        self.required_building = required_building
        super().__init__(**kwargs)
