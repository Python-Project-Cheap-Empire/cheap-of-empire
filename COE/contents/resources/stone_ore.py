from COE.contents.entity_types import EntityTypes
from .stone import Stone
from .resource_exceptions import MethodNotPermittedException


class StoneOre(Stone):
    def __init__(self, position):
        super().__init__(
            amount=60,
            name="Stone ore",
            positions=position,
            hp=1,
            height=1,
            width=1,
            line_of_sight=0,
            entity_type=EntityTypes.GROUND,
            sub_entities=[],
        )

    def increase_amount(self, amount):
        raise MethodNotPermittedException
