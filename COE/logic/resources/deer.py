from .cuttable_animal import CuttableAnimal
from .resource_exceptions import MethodNotPermittedException


class Deer(CuttableAnimal):
    def __init__(self, **kwargs):
        super().__init__(amount=55, **kwargs)
        self.amount = 55

    def increase_amount(self, amount):
        raise MethodNotPermittedException
