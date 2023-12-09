Simulating Evolutionary Dynamics of Decision-Making Agents
This code implements a mathematical model from Toupo et al. (2015) analyzing periodic dynamics between controlled and automatic decision-making agent populations. The system of differential equations explores evolutionary game theory concepts, including competitive advantages and diminishing returns, to determine conditions that enable agent type coexistence or oscillations.

**Model Overview**
The primary state variables are:

* x(t): Fraction of controlled agents
* β(t): Competitive advantage of automatic agents

Key parameters:

ρ: Probability of locating resources
α: Extent of diminishing returns
τ: Lag on state impacts

See the original paper for full model details.


**Usage:**

The simulation is implemented in Python. To run:

```Terminal
python src\simulate_agents.py
```

The script loads parameters, integrates the equations, and plots the results. See the code for analysis details.

**Extensions:**
Potential areas for further exploration:

* Adding stochasticity
* Incorporating more agent heuristics
* Comparing to evolutionary multi-agent simulations

This model provides a baseline to study decision-making dynamics under environmental pressures.

**References:**

Toupo, D.F., Strogatz, S.H., Cohen, J.D. and Rand, D.G., 2015. Evolutionary game dynamics of controlled and automatic decision-making. Chaos: An Interdisciplinary Journal of Nonlinear Science, 25(7), pp.073120.

Let me know if you would like any sections expanded or additional contributor guidelines included! Aimed to provide an overview for researchers interested in implementing and modifying the paper's model.
