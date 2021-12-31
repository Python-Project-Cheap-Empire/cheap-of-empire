from .stone import Stone
from .resource_exceptions import MethodNotPermittedException


class StoneOre(Stone):
    def __init__(self, **kwargs):
        super().__init__(amount=60, **kwargs)

    def increase_amount(self, amount):
        raise MethodNotPermittedException
