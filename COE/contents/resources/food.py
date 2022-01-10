from .resource import Resource
from COE.contents.entity import Entity
from .resource_type import ResourceType


class Food(Resource, Entity):
    def __init__(self, position, **kwargs):
        Resource.__init__(self, r_type=ResourceType.FOOD, **kwargs)
        Entity.__init__(self, positions=position, **kwargs)
