from .resource import Resource
from COE.contents.entity import Entity
from .resource_type import ResourceType


class Food(Resource, Entity):
    def __init__(self, **kwargs):
        super().__init__(r_type=ResourceType.FOOD, **kwargs)
