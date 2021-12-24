from COE.logic.resources import *
import pytest


def test_tree():
    acacia = Tree(
        name="Acacia",
        hp=1,
        positions=(10, 15),
        height=1,
        width=1,
        line_of_sight=0,
        img=None,
    )
    assert acacia.type == ResourceType.WOOD
    assert acacia.amount == 60

    acacia.decrease_amount(60)
    assert acacia.amount == 0

    with pytest.raises(MethodNotPermittedException):
        acacia.increase_amount(5)


def test_gold_ore():
    goldy = GoldOre(
        name="Gold Ore",
        hp=1,
        positions=(10, 15),
        height=1,
        width=1,
        line_of_sight=0,
        img=None,
    )
    assert goldy.type == ResourceType.GOLD
    assert goldy.amount == 60

    goldy.decrease_amount(30)
    assert goldy.amount == 30

    with pytest.raises(MethodNotPermittedException):
        goldy.increase_amount(5)


def test_stone_ore():
    pierre = StoneOre(
        name="stony",
        hp=50,
        positions=(10, 15),
        height=10,
        width=10,
        line_of_sight=0,
        img=None,
    )
    assert pierre.type == ResourceType.STONE
    assert pierre.amount == 60

    pierre.decrease_amount(59)
    assert pierre.amount == 1

    with pytest.raises(MethodNotPermittedException):
        pierre.increase_amount(5)


def test_berry():
    strawberry = Berry(
        name="Strawberry",
        hp=1,
        positions=(10, 15),
        height=2,
        width=2,
        line_of_sight=0,
        img=None,
    )

    assert strawberry.type == ResourceType.FOOD
    assert strawberry.amount == 40

    with pytest.raises(MethodNotPermittedException):
        strawberry.increase_amount(5)


def test_deer():
    bambi = Deer(
        name="Bambi",
        hp=50,
        positions=(10, 15),
        height=1,
        width=1,
        line_of_sight=0,
        img=None,
    )

    with pytest.raises(MethodNotPermittedException):
        bambi.increase_amount(5)

    assert bambi.amount == 55
