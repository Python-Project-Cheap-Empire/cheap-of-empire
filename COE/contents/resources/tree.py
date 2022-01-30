from COE.contents.entity_types import EntityTypes
from .wood import Wood
from .resource_exceptions import MethodNotPermittedException


class Tree(Wood):
    def __init__(self, position):
        super().__init__(
            name="Tree",
            amount=60,
            positions=position,
            hp=-1,
            height=1,
            width=1,
            line_of_sight=0,
            entity_type=EntityTypes.GROUND,
            sub_entities=[],
        )

    def increase_amount(self, amount):
        raise MethodNotPermittedException
