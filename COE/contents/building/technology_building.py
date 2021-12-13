from .building import Building


class TechnologyBuilding(Building):
    # def __init__(self):
    #     super.__init__(self)

    def __init__(self, required: set, **kwargs):
        self.required = required
        super().__init__(**kwargs)
