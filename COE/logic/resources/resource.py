from .resource_exceptions import *
from .resource_type import ResourceType


class Resource:
    """A Resource is represented by a resource type and an amount"""

    def __init__(self, r_type: ResourceType, amount: int, **kwargs):
        """Constructor for a resource:
        @:param type
        @:param amount
        """
        self.type = r_type
        self.amount = amount

    @property
    def type(self):
        return self.type

    @property
    def value(self):
        return self.value

    def increase_amount(self, amount):
        if self.value > 9999:
            raise MaximumResourceException
        self.value += amount

    def decrease_amount(self, amount):
        if self.value - amount < 0:
            raise NotEnoughResourceException
        self.value -= amount
