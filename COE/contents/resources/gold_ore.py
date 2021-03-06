from COE.contents.entity_types import EntityTypes
from .gold import Gold
from .resource_exceptions import MethodNotPermittedException


class GoldOre(Gold):
    def __init__(self, position):
        super().__init__(
            amount=60,
            name="Gold ore",
            positions=position,
            hp=-1,
            height=1,
            width=1,
            line_of_sight=0,
            entity_type=EntityTypes.GROUND,
        )

    def increase_amount(self, amount):
        raise MethodNotPermittedException
