from even__odd import check_even_odd
def test_even():
    assert check_even_odd(10)=="even"
def test_odd():
    assert check_even_odd(7)=="odd"
def test_zero():
    assert check_even_odd(0)=="even"
def test_negative():
    assert check_even_odd(-4)=="even"        