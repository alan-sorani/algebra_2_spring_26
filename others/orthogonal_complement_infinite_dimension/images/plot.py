import numpy as np
import matplotlib.pyplot as plt

# Domain
x = np.linspace(-1, 1, 2000)

# Continuous function g on [-1, 1]
def g(x):
    return x * np.sin(x) + x**3 * np.cos(x)


# Choose x_0 such that g(x_0) > 0
x_0 = 0.5

# Open interval (a, b) containing x_0
a, b = 0.3, 0.7

# Midpoint and radius of the interval
center = (a + b) / 2
radius = (b - a) / 2


# Smooth exponential bump
def exponential_bump(x):
    values = np.zeros_like(x, dtype=float)
    inside = (a < x) & (x < b)

    exponent = (
        -1 / ((x[inside] - a) * (b - x[inside]))
        + 1 / ((center - a) * (b - center))
    )

    values[inside] = 0.65 * np.exp(exponent)
    return values


# Sine bump
def sine_bump(x):
    values = np.zeros_like(x, dtype=float)
    inside = (a < x) & (x < b)

    values[inside] = 0.50 * np.sin(
        np.pi * (x[inside] - a) / (b - a)
    )

    return values


# Polynomial bump
def polynomial_bump(x):
    values = np.zeros_like(x, dtype=float)
    inside = (a < x) & (x < b)

    normalized_x = (x[inside] - center) / radius
    values[inside] = 0.35 * (1 - normalized_x**2) ** 2

    return values


exponential_label = (
    r"$f_1(x)=0.65\exp\left("
    r"-\frac{1}{(x-0.3)(0.7-x)}+25"
    r"\right)$"
    "\n"
    r"for $0.3<x<0.7$, and $f_1(x)=0$ otherwise"
)

sine_label = (
    r"$f_2(x)=0.50\sin\left("
    r"\frac{\pi(x-0.3)}{0.4}"
    r"\right)$"
    "\n"
    r"for $0.3<x<0.7$, and $f_2(x)=0$ otherwise"
)

polynomial_label = (
    r"$f_3(x)=0.35\left("
    r"1-\left(\frac{x-0.5}{0.2}\right)^2"
    r"\right)^2$"
    "\n"
    r"for $0.3<x<0.7$, and $f_3(x)=0$ otherwise"
)


fig, ax = plt.subplots(figsize=(11, 7))

ax.plot(
    x,
    g(x),
    linewidth=2.5,
    label=r"$g(x)=x\sin(x)+x^3\cos(x)$",
)

ax.plot(
    x,
    exponential_bump(x),
    linewidth=2,
    linestyle="--",
    label=exponential_label,
)

ax.plot(
    x,
    sine_bump(x),
    linewidth=2,
    linestyle=":",
    label=sine_label,
)

ax.plot(
    x,
    polynomial_bump(x),
    linewidth=2,
    linestyle="-.",
    label=polynomial_label,
)

# Mark x_0 and g(x_0)
ax.scatter(
    [x_0],
    [g(x_0)],
    zorder=5,
    label=rf"$x_0={x_0},\quad g(x_0)\approx {g(x_0):.3f}>0$",
)

# Mark and shade the open interval
ax.axvline(a, linestyle=":", alpha=0.7)
ax.axvline(b, linestyle=":", alpha=0.7)

ax.axvspan(
    a,
    b,
    alpha=0.08,
    label=rf"Open interval $({a},{b})$",
)

ax.axhline(0, linewidth=0.8)

ax.set_xlim(-1, 1)
ax.set_ylim(-0.1, 1.45)
ax.set_xlabel(r"$x$")
ax.set_ylabel("Function value")
ax.grid(alpha=0.25)

ax.legend(loc="upper left", fontsize=9)

fig.tight_layout()
fig.savefig("bump_functions.png", bbox_inches="tight")
plt.show()
