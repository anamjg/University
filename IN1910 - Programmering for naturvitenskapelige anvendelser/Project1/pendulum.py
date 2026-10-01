# Exercises part 2
from dataclasses import dataclass
from turtle import Pen
import numpy as np
import matplotlib.pyplot as plt

from typing import Optional
from scipy.integrate import solve_ivp

from ode import ODEModel, ODEResult, solve_ode, plot_ode_solution


class Pendulum(ODEModel):
    def __init__(self,  M=1, g = 9.81, L: Optional[float] = None):
        if L == None:
            L = 1
        self.L = L
        self.M = M
        self.g = g

    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        
        theta, omega = u
        dθ_dt = omega
        
        dw_dt = -self.g/self.L*np.sin(theta)
        return np.array([dθ_dt, dw_dt])

    @property
    def num_states(self) -> int:
        return 2


@dataclass
class PendulumResults:
    results: ODEResult
    pendant: Pendulum
    
    @property
    def theta(self):
        return self.results.solution[0]
    
    @property
    def omega(self):
        return self.results.solution[1]
    
    @property
    def x(self):
        x = self.pendant.L * np.sin(self.theta)
        return x
    
    @property
    def y(self):
        return -self.pendant.L * np.cos(self.theta)
    
    @property
    def potential_energy(self):
        P = self.pendant.M * self.pendant.g * (self.y + self.pendant.L)
        return P
    
    @property
    def vx(self):
        vx = np.gradient(self.x, self.results.time)
        return vx
    
    @property
    def vy(self):
        vy = np.gradient(self.y, self.results.time)
        return vy

    @property
    def kinetic_energy(self):
        K = 0.5*(self.vx*self.vx + self.vy*self.vy)
        return K
    
    @property
    def total_energy(self):
        energy = self.kinetic_energy + self.potential_energy
        return energy
    

class DampenedPendulum(Pendulum):
    def __init__(self, B, L=1, g=9.81, M=1):
        Pendulum.__init__(self, L, g, M, )
        self.B = B
        
    def __call__(self, t: float, u: np.ndarray) -> np.ndarray:
        theta, omega = u
        dθ_dt = omega
        
        dw_dt = -self.g/self.L*np.sin(theta) - self.B*omega
        return np.array([dθ_dt, dw_dt])

def exercise_2b():
    pedant = Pendulum()
    theta = np.pi/6
    omega = 0.35
    u0 = np.array([theta, omega])
    T = 10
    dt = 0.01
    
    sol = solve_ode(pedant, u0, T, dt)
    plot_ode_solution(
        sol, 
        [r"$\theta$", r"$\omega$"],
        filename='exercise_2b.png'
    )

def solve_pendulum(
    u0: np.ndarray,
    T: float,
    dt: float = 0.01,
    pendant: Optional[Pendulum] = None
) -> PendulumResults:
    pendant = Pendulum()
    time, sol = solve_ode(pendant, u0, T, dt)
    result = PendulumResults(ODEResult(time, sol), pendant)
    return result
    
def plot_energy(results: PendulumResults, filename: Optional[str] = None) -> None:
    labels = ['Potential Energy', 'Kinetic Energy', 'Total Energy']
    
    plt.plot(results.potential_energy)
    plt.plot(results.kinetic_energy)
    plt.plot(results.total_energy)
    
    plt.xlabel('Time')
    plt.ylabel('Energy')
    plt.grid()
    plt.legend(labels)
    
    if filename == None:
        plt.show()
    
    plt.savefig(filename)
    
def exercise_2g():
    u0 = np.array([np.pi/6, 0.35])
    T = 10
    dt = 0.01
    pendant = Pendulum()
    sol = solve_ode(pendant, u0, T, dt)
    results = PendulumResults(sol, pendant)
    filename = 'energy_single.png'
    plot_energy(results, filename)

def exercise_2h():
    u0 = np.array([np.pi/6, 0.35])
    T = 10
    dt = 0.01
    pendant = DampenedPendulum(B = 1)
    sol = solve_ode(pendant, u0, T, dt)
    results = PendulumResults(sol, pendant)
    filename = 'energy_damped.png'
    plot_energy(results, filename)
    
    
if __name__ == "__main__":
    exercise_2b()
    exercise_2g()
    exercise_2h()