import numpy as np
import matplotlib.pyplot as plt

def plot_func(f, a, b):
    """Plot a function f(x) from x=a to x=b."""
    x = np.linspace(a, b, 400)
    y = f(x)

    plt.figure()
    plt.plot(x, y, color="blue")
    plt.title(f"Plot of function from {a} to {b}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

# Example usage:
plot_func(lambda x: np.sin(x), 0, 2 * np.pi)
