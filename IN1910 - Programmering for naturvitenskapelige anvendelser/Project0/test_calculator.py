from calculator import *
import pytest
from math import pi, sqrt


@pytest.mark.parametrize("arg1, arg2, output", [(1, 2, 3), (0.1, 0.2, 0.3)])
def test_add(arg1, arg2, output):
    assert add(arg1, arg2) == pytest.approx(output)

@pytest.mark.parametrize("arg1, arg2, output", [(4, 2, 2), (6, 2, 3)])
def test_div(arg1, arg2, output):    
    assert div(arg1, arg2) == output


@pytest.mark.parametrize("arg, output", [(4, 24), (1, 1), (0, 1)])
def test_fac(arg, output):
    assert fac(arg) == output

@pytest.mark.parametrize("arg, output", [(0, 0), (pi/4, 1/sqrt(2)), (pi/2, 1), (3*pi/2, -1)])
def test_sinus(arg, output):
    assert sinus(arg) == pytest.approx(output)
    
@pytest.mark.parametrize("arg, output", [(9, 3), (4, 2)])
def test_square_root(arg, output):
    assert square_root(arg) == output
 
def test_factorial_raises_ValueError_for_negatives():
    try:
        div(3,0)
    except ValueError:
        # Correct exception is raised, test should pass
        pass
    except ZeroDivisionError:
        # Correct exception is raised, test should pass
        pass
    except Exception:
        # This catches any other type of exception, test should fail
        raise Exception
    else:
        # No exception has been raised, test should fail
        raise Exception

    
def test_is_float_raises_ValueError_for_string_arguments():
    with pytest.raises(ValueError):
        fac(-1)
 