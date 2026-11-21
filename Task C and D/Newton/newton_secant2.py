from scipy.optimize import root_scalar

# Modified investment cash flows
cash_flows = [-12000, 3500, 4000, 4500, 4000]

# Net Present Value function
def npv(rate):
    return sum(
        cf / (1 + rate)**t
        for t, cf in enumerate(cash_flows)
    )

# Derivative of NPV
def d_npv(rate):
    return sum(
        -t * cf / (1 + rate)**(t + 1)
        for t, cf in enumerate(cash_flows)
        if t > 0
    )

# Newton-Raphson method
newton = root_scalar(
    npv,
    fprime=d_npv,
    x0=0.10,
    method="newton",
    xtol=1e-12
)

# Secant method
secant = root_scalar(
    npv,
    x0=0.05,
    x1=0.20,
    method="secant",
    xtol=1e-12
)

print(f"IRR using Newton-Raphson: {newton.root:.6%}")
print(f"IRR using Secant method:  {secant.root:.6%}")
print(f"NPV at Newton solution:   {npv(newton.root):.6f}")