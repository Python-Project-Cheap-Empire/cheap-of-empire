from COE.logic.resources import *


def test_wood():
    woody = Wood(
        amount=40,
        name="woody",
        hp=50,
        positions=(10, 15),
        height=10,
        width=10,
        line_of_sight=0,
        img=None,
    )
    assert woody.type == ResourceType.WOOD


def test_gold():
    goldy = Gold(
        amount=40,
        name="goldy",
        hp=50,
        positions=(10, 15),
        height=10,
        width=10,
        line_of_sight=0,
        img=None,
    )
    assert goldy.type == ResourceType.GOLD


def test_stone():
    stony = Stone(
        amount=40,
        name="stony",
        hp=50,
        positions=(10, 15),
        height=10,
        width=10,
        line_of_sight=0,
        img=None,
    )
    assert stony.type == ResourceType.STONE


def test_food():
    foody = Food(
        amount=40,
        name="foody",
        hp=50,
        positions=(10, 15),
        height=10,
        width=10,
        line_of_sight=0,
        img=None,
    )
    assert foody.type == ResourceType.FOOD
