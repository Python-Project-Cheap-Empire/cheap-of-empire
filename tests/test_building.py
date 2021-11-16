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
)


def test_archery_range():
    a = ArcheryRange()

    assert a.unit_type == ""

    a.train_bowman()
    a.train_bowman()
    assert a.pending_units == ["BowMan", "BowMan"]
    # assert a.required == {"Long Bow"}


def test_barrack():
    b = Barrack()
    b.train_axeman()
    b.train_clubman()
    b.train_slinger()
    assert b.pending_units == ["AxeMan", "ClubMan", "Slinger"]
    assert b.upgrade_technology() == "Upgrading..."


def test_building():
    b = Building()
    assert b.img == "None"


def test_dock():
    d = Dock()
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


def test_farm():
    f = Farm(175)
    assert f.ressource == 175
    assert f.re_seeding_farm() == "ReSeeding Farm"


def test_granary():
    g = Granary()
    assert g.upgrade_technology() == "Upgrading..."


def test_market():
    m = Market()
    m.enable_tribute()
    assert m.enabled_tribute
    assert m.research_economic_technology() == "Research Economic Technologies"


def test_military_building():
    ml = MilitaryBuilding()
    assert ml.img == "None"


def test_stable():
    s = Stable()
    s.train_scout()
    s.train_scout()
    assert s.pending_units == ["Scout", "Scout"]
    assert s.upgrade_technology() == "Upgrading..."


def test_storage_building():
    sb = StorageBuilding(0, 0)
    assert sb.ressources == 0
    assert sb.max_held == 0


def test_storage_pit():
    sp = StoragePit()
    assert sp.upgrade_technology() == "Upgrading..."
    assert sp.is_drop_point


def test_technology_building():
    tb = TechnologyBuilding()
    assert tb.img == "None"


def test_town_center():
    tc = TownCenter(True, 6)
    assert tc.advance_age() == "Advancing Age..."
    tc.train_villager()
    tc.train_villager()
    assert tc.pending_units == ["Villager", "Villager"]


test_archery_range()
test_barrack()
test_building()
test_dock()
test_farm()
test_granary()
test_market()
test_military_building()
test_stable()
test_storage_building()
test_storage_pit()
test_technology_building()
test_town_center()
