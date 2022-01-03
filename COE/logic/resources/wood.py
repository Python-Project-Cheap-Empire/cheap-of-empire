from .resource import Resource
from COE.contents.entity import Entity
from .resource_type import ResourceType


class Wood(Resource, Entity):
    def __init__(self, amount, **kwargs):
        Resource.__init__(self, r_type=ResourceType.WOOD, amount=amount)
        Entity.__init__(self, **kwargs)
