import mathlib
import pytest # type: ignore

def test_calc_total():
    total = mathlib.calc_total(4,5)
    assert total==9

def test_multiply():
    total = mathlib.multiply(4,5)
    assert total==20


# pytest fixtures
@pytest.fixture()
def cur():
    return "hello"

# now adding "cur" as parameter will automatically call cur fxn and returns the  value in the variable
def test_with_fxture(cur):
    total = mathlib.calc_total(4,5)
    print(cur)
    assert total==9

# using multiple parameter in a single function
@pytest.mark.parametrize("a, b, expected",[
    (1,2,3),
    (0,0,0),
    (-1,1,0),
])
def test_add(a,b,expected):
    assert mathlib.calc_total(a,b) == expected