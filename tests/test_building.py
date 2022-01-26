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


def test_archery_range():
    a = ArcheryRange((0, 0))

    a.train_bowman()
    a.train_bowman()
    assert a.pending_units == ["BowMan", "BowMan"]
    # assert a.required == {"Long Bow"}
    assert a.required_building == {Barrack.__class__.__name__}
    assert a.wood_required == 150
    assert a.time_construction == 40


def test_barrack():
    b = Barrack((0, 0))
    b.train_axeman()
    b.train_clubman()
    b.train_slinger()
    assert b.pending_units == ["AxeMan", "ClubMan", "Slinger"]
    assert b.upgrade_technology() == "Upgrading..."
    assert b.required_building == {TownCenter.__class__.__name__}
    assert b.wood_required == 130
    assert b.time_construction == 40


def test_dock():
    d = Dock((0, 0))
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
    assert d.time_construction == 40


def test_farm():
    f = Farm(175, (0, 0))
    assert f.resources == 175
    assert f.re_seeding_farm() == "ReSeeding Farm"
    assert f.max_held == 250
    assert f.required_building == {Market.__class__.__name__}
    assert f.wood_required == 75
    assert f.time_construction == 24


def test_granary():
    g = Granary((0, 0))
    assert g.upgrade_technology() == "Upgrading..."
    assert g.line_of_sight == 6
    assert g.required_age == 1
    assert g.wood_required == 120
    assert g.time_construction == 30


def test_market():
    m = Market((0, 0))
    m.enable_tribute()
    assert m.enabled_tribute
    assert m.research_economic_technology() == "Research Economic Technologies"
    assert m.required_age == 1
    assert m.required_researches == {}
    assert m.required_building == {Granary.__class__.__name__}
    assert m.wood_required == 150
    assert m.time_construction == 40


def test_stable():
    s = Stable((0, 0))
    s.train_scout()
    s.train_scout()
    assert s.pending_units == ["Scout", "Scout"]
    assert s.upgrade_technology() == "Upgrading..."
    assert s.wood_required == 150
    assert s.time_construction == 40


def test_storage_pit():
    sp = StoragePit((0, 0))
    assert sp.upgrade_technology() == "Upgrading..."
    assert sp.is_drop_point
    assert sp.wood_required == 120
    assert sp.time_construction == 30


def test_town_center():
    tc = TownCenter((0, 0), True)
    assert tc.advance_age() == "Advancing Age..."
    tc.train_villager()
    tc.train_villager()
    assert tc.pending_units == ["Villager", "Villager"]
    assert tc.required_building == {}
    assert tc.wood_required == 200
    assert tc.time_construction == 60


def test_house():
    h = House((0, 0))
    assert h.increase_max_population() == "Max pop +5"
    assert h.decrease_max_population() == "Max pop -5"
    assert h.required_age == 1
    assert h.required_researches == {}
    assert h.wood_required == 30
    assert h.time_construction == 15


def test_watch_tower():
    t = WatchTower((0, 0))
    assert t.attack(Entity("Enemy", 0, (0, 0), 1, 1, 1)) == "Attacking..."
    assert t.damage == 3
    assert t.required_age == 2
    assert t.required_building == {Granary.__class__.__name__}
    assert t.stone_required == 150
    assert t.wood_required == 0
    assert t.time_construction == 30


def test_small_wall():
    sw = SmallWall((0, 0))
    assert sw.name == "Small Wall"
    assert sw.hp == 100
    assert sw.wood_required == 20
    assert sw.time_construction == 10
