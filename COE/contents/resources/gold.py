from .resource import Resource
from COE.contents.entity import Entity
from .resource_type import ResourceType


class Gold(Resource, Entity):
    def __init__(self, **kwargs):
        Resource.__init__(self, r_type=ResourceType.GOLD, **kwargs)
        Entity.__init__(self, **kwargs)
