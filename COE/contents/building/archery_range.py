from COE.contents.entity import Entity
from .military_building import MilitaryBuilding
from .technology_building import TechnologyBuilding

# Require Barrack to be built
required_barrack = False


class ArcheryRange(MilitaryBuilding, TechnologyBuilding):
    def __init__(self):
        MilitaryBuilding.__init__(self, "", pending_units=[])
        TechnologyBuilding.__init__(self, required=set([""]))
        # if self.required.intersection({"Barrack"}) == "Barrack":
        #     print("Archery Range created")
        Entity.__init__(self, "ArcheryRange", 350, (0, 0), 1, 1, 6, "none")

    # def upgrade_technology(self, tech_name):
    #     archery_range_tech[tech_name] = True

    def train_bowman(self):
        self.pending_units.append("BowMan")


# p = ArcheryRange()
# p.train_bowman()
# print(p.pending_units)
