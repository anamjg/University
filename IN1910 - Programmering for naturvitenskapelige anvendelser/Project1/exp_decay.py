# Project 1 - IN1910
import numpy as np
from ode import ODEModel
import ode
from scipy.integrate import solve_ivp


class ExponentialDecay(ODEModel):
    def __init__(self, a):
        self.a = a

    @property
    def decay(self):
        return self._a

    @decay.setter
    def decay(self, a):
        if (a < 0):
            raise ValueError('The constant a cannot be negative.')
        self._a = a

    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        if len(u) != 1:
            raise AssertionError('The numpy array had not length 1.')
        else:
            return -self._a*u

    @property
    def num_states(self) -> int:
        return 1


def solve_exponential_decay(a, u0, t, dt):
    # use solve_ivp to solve the ODE
    t_span = (0, t)
    t_eval = np.arange(0, t, dt)
    model = ExponentialDecay(a)
    y0 = u0[0]
    sol = solve_ivp(model, t_span, y0, t_eval=t_eval)
    return sol


if __name__ == "__main__":
    model = ExponentialDecay(0.4)
    u = np.array([3.2])
    du_dt = model(0.0, u)
