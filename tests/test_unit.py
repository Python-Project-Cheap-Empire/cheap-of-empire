from COE.contents.unit.villager import Villager
from COE.contents.unit.axeman import Axeman
from COE.contents.unit.fishing_boat import FishingBoat
from COE.contents.unit.light_transport import LightTransport
from COE.contents.unit.scout import Scout
from COE.contents.unit.scout_ship import ScoutShip
from COE.contents.unit.slinger import Slinger
from COE.contents.unit.trade_boat import TradeBoat
from COE.contents.unit.bowman import Bowman
from COE.logic.Player import Player


def test_unit():
    p1 = Player("Player 1", True, [], [], None, None)
    p2 = Player("Player 2", True, [], [], None, None)
    v = Villager((2, 2), p2)
    b = Bowman((0, 0), p1)
    p1.units.append(b)
    p2.units.append(v)

    assert p1.units[0].check_in_range(p2.units[0])
    assert not p2.units[0].check_in_range(p1.units[0])
    p1.units[0].attacked_entity = p2.units[0]
    p1.units[0].is_attacking = True
    p1.units[0].attack()
    assert p2.units[0].hp == 46
    p2.units[0].hp = 0
    assert p2.units[0].die()
