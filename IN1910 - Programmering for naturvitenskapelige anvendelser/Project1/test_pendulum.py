# Test file part 2
import pytest
import numpy as np 

from pendulum import Pendulum, solve_pendulum
from ode import solve_ode


def test_unit_verification():
    expected_d0_dt = 0.35
    expected_dw_dt = -3.45423
    
    t = np.arange(0, 10, 0.01)
    theta = np.pi/6
    omega = 0.35
    
    pendant = Pendulum(L = 1.42)
    computed = pendant(t, (theta, omega))
    assert expected_d0_dt == pytest.approx(computed[0])
    assert abs(expected_dw_dt - computed[1]) < 1e-5
    
def test_equilibrium():
    t = np.arange(0, 10, 0.01)
    theta = 0
    omega = 0
    
    pendal = Pendulum(L = 1.42)
    calculated = pendal(t, (theta, omega))
    assert calculated[0] == 0
    assert calculated[1] == 0
    
def test_solve_pendulum_ode_with_zero_ic():
    pendant = Pendulum()
    u0 = np.array([0,0])
    T = 10
    dt = 0.01
    sol = solve_ode(pendant,u0,T,dt)
    assert list(sol.solution[0]) == [0] * sol.num_timepoints    
    assert list(sol.solution[1]) == [1] * sol.num_timepoints   
    
def test_solve_pendulum_function_zero_ic():
    u0 = np.array([0,0])
    solution = solve_pendulum(u0, T=10, dt=0.01, pendant=Pendulum(L=1.42))
    
    assert list(solution.theta) == [0] * solution.results.num_timepoints
    assert list(solution.omega) == [0] * solution.results.num_timepoints
    assert list(solution.x) == [0] * solution.results.num_timepoints
    assert list(solution.y) == [-1.42] * solution.results.num_timepoints
