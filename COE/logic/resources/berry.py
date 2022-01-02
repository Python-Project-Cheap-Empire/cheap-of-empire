from .food import Food
from .resource_exceptions import MethodNotPermittedException


class Berry(Food):
    def __init__(self, **kwargs):
        super().__init__(amount=40, **kwargs)

    def increase_amount(self, amount):
        raise MethodNotPermittedException
