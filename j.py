from scipy.optimize import root_scalar

# MRI Investment: Initial cost, followed by 4 years of patient revenue ($100k units)
cash_flows = [-10.0, 3.0, 3.5, 4.0, 2.5]

def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))

def d_npv(rate):
    return sum(-t * cf / (1 + rate)**(t + 1) for t, cf in enumerate(cash_flows) if t > 0)

# Newton-Raphson method
newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)

print(f"MRI Machine IRR (Newton-Raphson): {newton.root:.6%}")
print(f"NPV at this rate: {npv(newton.root):.6f}")