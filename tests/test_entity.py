from COE.contents.entity import Entity


def test_init():
    e = Entity("Tree", 10, (10, -10), 1, 1, 10)
    assert e.name == "Tree"
