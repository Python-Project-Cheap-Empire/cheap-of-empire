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

    def increase_amount(self, amount):
        if self.amount > 9999:
            raise MaximumResourceException
        self.amount += amount

    def decrease_amount(self, amount):
        if self.amount - amount < 0:
            raise NotEnoughResourceException
        self.amount -= amount
