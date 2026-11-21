# Task P: Ordinary Differential Equations — Euler's Method

## 1. Project Overview

This project demonstrates how Euler's Method can be used to approximate the solution of an ordinary differential equation (ODE).

The example models the growth of a fish population over 10 years using a simple mathematical model.

## 2. Mathematical Concept

An ordinary differential equation describes how a quantity changes with respect to another variable.

The fish population growth model is:

dP/dt = rP

Where:

- P = fish population
- t = time in years
- r = population growth rate
- dP/dt = rate of change of the population

For this example:

- Initial population, P₀ = 100 fish
- Growth rate, r = 0.2 per year
- Step size, h = 1 year
- Simulation period = 10 years

## 3. Euler's Method Formula

Euler's Method uses the formula:

P(n+1) = P(n) + h × f(t(n), P(n))

For the fish population model:

P(n+1) = P(n) + h × rP(n)

Using the initial values:

P₁ = 100 + 1 × (0.2 × 100)

P₁ = 120 fish

Therefore, the estimated population after one year is 120 fish.

## 4. Files Included

- `fish_population_euler.py` — Python program implementing Euler's Method.
- `README.md` — Project explanation, mathematical model, and instructions.

## 5. Requirements

The program requires Python 3 and the following libraries:

- NumPy
- Matplotlib

Install the libraries using:

```bash
python -m pip install numpy matplotlib
```

## 6. How to Run the Program

1. Open the project folder in VS Code.
2. Open the terminal.
3. Install the required libraries.
4. Run the program:

```bash
python fish_population_euler.py
```

The program prints the estimated population for each year and displays a graph of population growth against time.

## 7. Expected Output

The first few estimated values are:

| Year | Estimated population |
| ---: | -------------------: |
|    0 |                  100 |
|    1 |                  120 |
|    2 |                  144 |
|    3 |               172.80 |
|    4 |               207.36 |

The population increases because the model assumes that the growth rate is proportional to the current population.

The final numerical output should be checked by running the program.

## 8. Graph Interpretation

The graph shows time on the horizontal axis and the estimated fish population on the vertical axis.

The curve rises because the population grows at a rate proportional to its current size. As the population increases, the model predicts a larger increase during each subsequent year.

## 9. Changing a Parameter

The step size can be changed from:

```python
h = 1.0
```

to:

```python
h = 0.5
```

This uses half-year steps instead of one-year steps.

A smaller step size generally improves Euler's approximation for this smooth growth model, although it requires more calculations.

Run both versions and compare their results.

## 10. Assumptions and Limitations

The model assumes that:

- The initial population is 100 fish.
- The growth rate remains constant at 0.2 per year.
- Food and space are unlimited.
- There are no effects from disease, predators, or environmental changes.
- Population values are mathematical estimates and may be fractional.

These assumptions simplify the model. Actual fish populations may behave differently.

## 11. Conclusion

This project demonstrates the application of Euler's Method to a population growth problem.

The method estimates future population values using the current population, growth rate, and step size. It also demonstrates how changing the step size affects the numerical approximation.
