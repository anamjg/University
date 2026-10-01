import numpy as np
import abc
from typing import NamedTuple, Optional, List
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


class ODEModel(abc.ABC):
    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        raise NotImplementedError

    @property
    def num_states(self) -> int:
        raise NotImplementedError


class ODEResult(NamedTuple):
    time: np.ndarray
    solution: np.ndarray

    @property
    def num_states(self) -> int:
        return self.solution.shape[0]

    @property
    def num_timepoints(self) -> int:
        return self.solution.shape[1]


class InvalidInitialConditionError(RuntimeError):
    pass


def solve_ode(model: ODEModel, u0: np.ndarray, T: float, dt: float) -> ODEResult:
    t_span = (0, T)
    t_eval = np.arange(0, T, dt)
    y0 = np.array([u0])
    sol = solve_ivp(model, t_span, y0, t_eval=t_eval)
    result = ODEResult(time=sol.t, solution=sol.y)
    return result


def plot_ode_solution(
    results: ODEResult,
    state_labels: Optional[List[str]] = None,
    filename: Optional[str] = None,
) -> None:
    x = results.time
    y = results.solution[0]
    plt.plot(x, y)
    plt.xlabel('Time')
    plt.ylabel('ODE solution')
    plt.grid()
    if state_labels == None:
        for i in range(len(x)):
            plt.legend(f'State {i}')
    else:
        plt.legend(state_labels)
    if filename == None:
        plt.show()
    else:
        plt.savefig(filename)
