import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
lines = plt.plot(t, t, 'b-', t, t**2, 'r-', t, t**3, 'g-', linewidth=2.0)

plt.setp(lines, color='r', linewidth=2.0)

# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)

plt.show()