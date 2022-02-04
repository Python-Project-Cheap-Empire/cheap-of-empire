from COE.contents.entity import Entity
from COE.contents.building import (
    ArcheryRange,
    Barrack,
    Building,
    Dock,
    Farm,
    Granary,
    Market,
    MilitaryBuilding,
    Stable,
    StorageBuilding,
    StoragePit,
    TechnologyBuilding,
    TownCenter,
    House,
    WatchTower,
    SmallWall,
)
from COE.map.enum.map_sizes import MapSizes
from COE.map.enum.map_types import MapTypes
from COE.map.enum.resources_rarity import ResourcesRarity
from COE.map.map import Map


def test_archery_range():
    a = ArcheryRange((0, 0), None)

    a.train_bowman()
    a.train_bowman()
    assert a.required_building == {Barrack.__class__.__name__}
    assert a.wood_required == 150
    assert a.construction_time == 40


def test_barrack():
    b = Barrack((0, 0), None)
    assert b.required_building == {TownCenter.__class__.__name__}
    assert b.wood_required == 130
    assert b.construction_time == 40


def test_dock():
    d = Dock((0, 0), None)
    d.train_fishing_boat()
    d.train_trade_boat()
    d.train_scout_ship()
    d.train_light_transport()
    assert d.pending_units == [
        "FishingBoat",
        "TradeBoat",
        "ScoutShip",
        "LightTransport",
    ]
    assert d.upgrade_technology() == "Upgrading..."
    assert d.required_building == {TownCenter.__class__.__name__}
    assert d.wood_required == 100
    assert d.construction_time == 40


def test_farm():
    f = Farm(175, (0, 0), None)
    assert f.resources == 175
    assert f.re_seeding_farm() == "ReSeeding Farm"
    assert f.max_held == 250
    assert f.required_building == {Market.__class__.__name__}
    assert f.wood_required == 75
    assert f.construction_time == 24


def test_granary():
    g = Granary((0, 0), None)
    assert g.upgrade_technology() == "Upgrading..."
    assert g.line_of_sight == 6
    assert g.required_age == 1
    assert g.wood_required == 120
    assert g.construction_time == 30


def test_market():
    m = Market((0, 0), None)
    m.enable_tribute()
    assert m.enabled_tribute
    assert m.research_economic_technology() == "Research Economic Technologies"
    assert m.required_age == 1
    assert m.required_researches == {}
    assert m.required_building == {Granary.__class__.__name__}
    assert m.wood_required == 150
    assert m.construction_time == 40


def test_stable():
    s = Stable((0, 0), None)
    s.train_scout()
    s.train_scout()
    assert s.pending_units == ["Scout", "Scout"]
    assert s.upgrade_technology() == "Upgrading..."
    assert s.wood_required == 150
    assert s.construction_time == 40


def test_storage_pit():
    sp = StoragePit((0, 0), None)
    assert sp.upgrade_technology() == "Upgrading..."
    assert sp.wood_required == 120
    assert sp.construction_time == 30


def test_town_center():
    tc = TownCenter((0, 0), None)
    assert tc.required_building == {}
    assert tc.wood_required == 200
    assert tc.construction_time == 60


def test_house():
    h = House((0, 0), None)
    assert h.increase_max_population() == "Max pop +5"
    assert h.decrease_max_population() == "Max pop -5"
    assert h.required_age == 1
    assert h.required_researches == {}
    assert h.wood_required == 30
    assert h.construction_time == 15


def test_watch_tower():
    t = WatchTower((0, 0), None)
    assert t.damage == 3
    assert t.required_age == 2
    assert t.required_building == {Granary.__class__.__name__}
    assert t.stone_required == 150
    assert t.wood_required == 0
    assert t.construction_time == 30


def test_small_wall():
    sw = SmallWall((0, 0), None)
    assert sw.name == "Small Wall"
    assert sw.hp == 100
    assert sw.wood_required == 20
    assert sw.construction_time == 10
