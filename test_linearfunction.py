def test_linearfunction():
    from linearfunction import linearfunction
    output = linearfunction((0, 0), (1, 1), 2)
    expected = 2
    assert output == expected


def test_point_on_line():
    from linearfunction import point_on_line
    output = point_on_line((0, 0), (1, 1), (2, 2))
    expected = True
    assert output == expected

    output = point_on_line((0, 0), (1, 1), (2, 0))
    expected = False
    assert output == expected
