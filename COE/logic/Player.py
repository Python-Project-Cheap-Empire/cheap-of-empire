class Player:
    """
    A class to represent a player.

    """

    # TODO : Create resource object in init. Waiting for class to be created
    def __init__(
        self,
        username: str,
        units: list,
        buildings: list,
        age,
        civilization,
        gold_amount: int = 500,
        wood_amount: int = 300,
        stone_amount: int = 300,
        food_amount: int = 300,
    ):
        """
        Constructs all the necessary attributes for the Player object.

        :param username: str
        :param gold_amount: int
        :param wood_amount: int
        :param stone_amount: int
        :param food_amount: int
        :param units: list
        :param buildings: list
        :param age: Age
        :param civilization: Civilization
        """
        self._username = username
        self._gold = gold_amount
        self._wood = wood_amount
        self._stone = stone_amount
        self._food = food_amount
        self._units = units
        self._buildings = buildings
        self._age = age
        self._civilization = civilization

    ###########
    # Getters #
    ###########
    @property
    def username(self):
        return self._username

    @property
    def gold(self):
        return self._gold

    @property
    def wood(self):
        return self._food

    @property
    def stone(self):
        return self._stone

    @property
    def food(self):
        return self._food

    @property
    def units(self):
        return self._units

    @property
    def buildings(self):
        return self._buildings

    @property
    def age(self):
        return self._age

    @property
    def civilization(self):
        return self._civilization
