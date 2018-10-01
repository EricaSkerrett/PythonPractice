def test_add_three():
    from simpleMath import add_three
    v1 = 1
    v2 = 2
    v3 = 3
    p = v1 + v2 + v3
    assert p == 5


def test_divide_sum():
    from simpleMath import divide_sum
    v1 = 6
    p = v1/3
    assert p == 2
