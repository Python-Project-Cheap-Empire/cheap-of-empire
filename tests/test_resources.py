from COE.contents.resources import *
import pytest


def test_tree():
    acacia = Tree((10, 15))

    assert acacia.type == ResourceType.WOOD
    assert acacia.amount == 60
    assert acacia.positions == (10, 15)
    assert acacia.name == "Tree"
    assert acacia.line_of_sight == 0
    assert acacia.hp == 1
    assert acacia.width == 1
    assert acacia.height == 1

    acacia.decrease_amount(60)
    assert acacia.amount == 0

    with pytest.raises(MethodNotPermittedException):
        acacia.increase_amount(5)


def test_gold_ore():
    goldy = GoldOre((10, 50))
    assert goldy.type == ResourceType.GOLD
    assert goldy.amount == 60
    assert goldy.positions == (10, 50)
    assert goldy.name == "Gold ore"
    assert goldy.hp == 1
    assert goldy.width == 1
    assert goldy.height == 1
    assert goldy.line_of_sight == 0

    goldy.decrease_amount(30)
    assert goldy.amount == 30

    with pytest.raises(MethodNotPermittedException):
        goldy.increase_amount(5)


def test_stone_ore():
    pierre = StoneOre((10, 15))
    assert pierre.type == ResourceType.STONE
    assert pierre.amount == 60
    assert pierre.positions == (10, 15)
    assert pierre.name == "Stone ore"
    assert pierre.hp == 1
    assert pierre.width == 1
    assert pierre.height == 1
    assert pierre.line_of_sight == 0

    pierre.decrease_amount(59)
    assert pierre.amount == 1

    with pytest.raises(MethodNotPermittedException):
        pierre.increase_amount(5)


def test_berry():
    strawberry = Berry((15, 10))

    assert strawberry.type == ResourceType.FOOD
    assert strawberry.amount == 40
    assert strawberry.positions == (15, 10)
    assert strawberry.name == "Berry"
    assert strawberry.hp == 1
    assert strawberry.width == 1
    assert strawberry.height == 1
    assert strawberry.line_of_sight == 0

    with pytest.raises(MethodNotPermittedException):
        strawberry.increase_amount(5)


def test_deer():
    bambi = Deer((12, 78))

    assert bambi.positions == (12, 78)
    assert bambi.name == "Deer"
    assert bambi.hp == 25
    assert bambi.width == 1
    assert bambi.height == 1
    assert bambi.line_of_sight == 0
    assert bambi.speed == 1.5

    assert bambi.state is None
    bambi.death()
    assert type(bambi.state) is CuttableAnimal

    assert bambi.state.amount == 55
    bambi.decrease_amount(10)
    assert bambi.state.amount == 45

    assert bambi.state.name == "Dead deer"
