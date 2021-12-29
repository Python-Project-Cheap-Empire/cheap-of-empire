from .food import Food
from COE.contents.unit.unit import Unit


class CuttableAnimal(Food):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
