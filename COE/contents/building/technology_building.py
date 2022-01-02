from .building import Building


class TechnologyBuilding(Building):
    # def __init__(self):
    #     super.__init__(self)

    def __init__(self, researches: set, **kwargs):
        self.researches = researches
        super().__init__(**kwargs)
