def test_hdl_analysis():
    from blood_analysis import hdl_analysis
    ans = hdl_analysis(70)
    expected = "Good"
    assert ans == expected


def test_hdl_analysis_borderline():
    from blood_analysis import hdl_analysis
    ans = hdl_analysis(45)
    expected = "Borderline"
    assert ans == expected


def test_hdl_analysis_bad():
    from blood_analysis import hdl_analysis
    ans = hdl_analysis(30)
    expected = "Bad"
    assert ans == expected


def test_ldl_analysis_bad():
    from blood_analysis import ldl_analysis
    ans = ldl_analysis(30)
    expected = "Normal"
    assert ans == expected
