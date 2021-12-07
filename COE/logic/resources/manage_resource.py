from . import ResourceType
from . import Resource


class ManageResource:
    """ Class holding the 4 types of resources"""
    def __init__(self, wood_amount, food_amount, gold_amount, stone_amount):
        self.wood = Resource(ResourceType.WOOD, wood_amount)
        self.food = Resource(ResourceType.FOOD, food_amount)
        self.gold = Resource(ResourceType.GOLD, gold_amount)
        self.stone = Resource(ResourceType.STONE, stone_amount)
