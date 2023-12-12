import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# Define ODE equations
def agent_odes(state, t):
    x, beta = state
    dx_dt = (
        (x - 1)
        * x
        * (
            a / (a - beta * rho + rho + beta * rho * x)
            + (rho + beta * rho * x) / (a + 1)
            - 1
        )
    )
    dbeta_dt = (x - beta) / tau
    return [dx_dt, dbeta_dt]

def plot_results(x, t):
    fig, ax = plt.subplots()
    ax.plot(t, x, "b-", label="x")
    ax.plot(t, 1 - x, "r--", label="1-x")
    ax.set_xlabel("Time")
    ax.set_ylabel("Fraction")
    ax.legend()
    plt.show()

def run_simulation(agent_odes, init_state, t):
    state = odeint(agent_odes, init_state, t)
    x = state[:, 0]
    beta = state[:, 1]
    return x, beta

def calculate_period(x):
    peaks = np.where(np.diff(np.sign(np.diff(x[1:]))) < 0)[0] + 1
    periods = np.diff(peaks)
    print("periods:", periods)
    period = np.average(periods)
    return peaks,period

def calculate_dominance_time(x, peaks):
    dom_times = []
    for i in range(len(peaks) - 1):
        x_slice = x[peaks[i] : peaks[i + 1]]
        x_dom = np.where(x_slice > 0.5)[0]
        dom_times.append(len(x_dom))
    domination_time = np.average(dom_times[1:])
    return domination_time

if __name__ == "__main__":
    # Problem parameters
    a = 0.75
    rho = 0.27  #  0.2 < rho < 0.3
    tau = 250  #  tau > 200

    # Initial conditions
    x0 = 0.7
    beta0 = 0.3
    init_state = [x0, beta0]

    # Time steps
    T = 6000
    t = np.linspace(0, T, T + 1)
    
    x, beta = run_simulation(agent_odes, init_state, t)
    plot_results(x, t)
    peaks, period = calculate_period(x)
    domination_time = calculate_dominance_time(x, peaks)

    print("Average period:", period)
    print("Average domination time:", domination_time)
