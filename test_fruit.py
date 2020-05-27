import pytest


@pytest.mark.parametrize("fruit, expected", [("apple", True),
                                             ("banana", True),
                                             ("broccoli", False),
                                             (" apple", True),
                                             ("peach", True),
                                             ("pear.", True)])
def test_is_fruit(fruit, expected):
    from fruitcheck import is_fruit
    ans = is_fruit(fruit)
    assert ans == expected


def test_add():
    from fruitcheck import add
    ans = add(4, 3)
    assert ans == pytest.approx(7)
