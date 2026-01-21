import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(0, 10, 500)

# Two functions
y1 = np.sin(x)
y2 = np.sin(x) + 1

plt.figure()
plt.fill_between(x, y1, y2, color="skyblue", alpha=0.7)
plt.plot(x, y1, label="sin(x)", color="blue")
plt.plot(x, y2, label="sin(x) + 1", color="red")

plt.title("Area between two curves")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()