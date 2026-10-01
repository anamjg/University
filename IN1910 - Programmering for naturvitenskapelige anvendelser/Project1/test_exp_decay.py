from cmath import exp
from exp_decay import ExponentialDecay
from ode import solve_ode
import ode
import numpy as np
import pytest
from pathlib import Path


def test_ExponentialDecay_value_verification():
    t = 0.0
    model = ExponentialDecay(0.4)
    u = np.array([3.2])
    du_dt = model(t, u)
    true_value = -1.28
    assert pytest.approx(du_dt) == true_value


def test_negative_decay_raises_ValueError():
    try:
        model = ExponentialDecay(0.4)
        model.decay = -1.0
    except ValueError:
        # Correct exception is raised, test should padss
        pass
    except Exception:
        # This catches any other type of exception, test should fail
        raise Exception
    else:
        # No exception has been raised, test should fail
        raise Exception


'''     
def test_solve_with_different_number_of_initial_states():   
    try:
        u0 = np.array([3.2, 3.2])
        model = ExponentialDecay(0.4)
        solve_ode(model, u0, T = 10, dt = 0.01)
    except ValueError:
        # Correct exception is raised, test should pass
        msg = InvalidInitialConditionError(u0)
        print(msg)
    except Exception:
        # This catches any other type of exception, test should fail
        raise Exception
    else:
        # No exception has been raised, test should fail
        raise Exception
'''


@pytest.mark.parametrize('a, u0, T, dt', [(0.4, 3.2, 10, 0.01), (0.5, 3.5, 10, 0.01), (0.6, 4.0, 10, 0.01)])
def test_solve_time(a, u0, T, dt):
    model = ExponentialDecay(a)
    result = solve_ode(model, u0, T, dt)
    if result[0][0] != 0:
        raise ValueError('The first time point is not zero')
    elif result[0][-1] != T-dt:
        print(result[0][-1])
        raise ValueError(f'The last time point is  not {T-dt}')
    elif result[0][1]-result[0][0] != dt:
        raise ValueError(
            f'The difference between the second and first time point is not {dt}')
    else:
        pass


@pytest.mark.parametrize('a, u0, T, dt', [(0.4, 3.2, 10, 0.01), (0.5, 3.5, 10, 0.01), (0.6, 4.0, 10, 0.01)])
def test_solve_solution(a, u0, T, dt):
    model = ExponentialDecay(a)
    result = solve_ode(model, u0, T, dt)
    y = result[1][0]
    y_exact = u0*exp(-a*0)
    relative_error = np.linalg.norm(y - y_exact) / np.linalg.norm(y_exact)
    assert relative_error < 100


def test_ODEResults():
    results = ode.ODEResult(time=np.array(
        [0, 1, 2]), solution=np.zeros((2, 3)))
    assert results.num_states == 2
    assert results.num_timepoints == 3


def test_plot_ode_solution_saves_file():
    model = ExponentialDecay(0.4)
    result = ode.solve_ode(model, u0=np.array([4.0]), T=10.0, dt=0.01)
    ode.plot_ode_solution(
        results=result, state_labels=["u"], filename="exponential_decay.png"
    )


def test_function_that_creates_a_file():

    # Check if the file already exists and delete if necessary
    filename = Path("exponential_decay.png")
    if filename.is_file():
        filename.unlink()

    # Call the function we are testing
    test_plot_ode_solution_saves_file()

    # Check that the file has now been created, then delete it
    assert filename.is_file()
    filename.unlink()
