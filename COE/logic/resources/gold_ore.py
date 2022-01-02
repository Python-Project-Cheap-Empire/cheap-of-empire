from .gold import Gold
from .resource_exceptions import MethodNotPermittedException


class GoldOre(Gold):
    def __init__(self, **kwargs):
        super().__init__(amount=60, **kwargs)

    def increase_amount(self, amount):
        raise MethodNotPermittedException
