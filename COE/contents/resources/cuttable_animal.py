from .food import Food


class CuttableAnimal(Food):
    def __init__(self, name, amount, position):
        super().__init__(
            name=name,
            amount=amount,
            position=position,
            hp=0,
            height=1,
            width=1,
            line_of_sight=0,
        )
