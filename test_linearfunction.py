def test_linearfunction():
    from linearfunction import linearfunction
    output = linearfunction((0, 0), (1, 1), 2)
    expected = 2
    assert output == expected
