from COE.contents.entity_types import EntityTypes
from .food import Food
from .resource_exceptions import MethodNotPermittedException


class Berry(Food):
    def __init__(self, position):
        super().__init__(
            amount=40,
            position=position,
            name="Berry",
            hp=1,
            height=1,
            width=1,
            line_of_sight=0,
            entity_type=EntityTypes.GROUND,
            sub_entities=[],
        )

    def increase_amount(self, amount):
        raise MethodNotPermittedException
