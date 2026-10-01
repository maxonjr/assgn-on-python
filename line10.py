import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
lines = plt.plot(t, t, 'rx', t, t**2, 'b*', t, t**3, 'g-', linewidth=2.0)

plt.setp(lines, color='r', linewidth=2.0)
plt.xlabel('Dummy data for x')
plt.title('An example graph')
plt.text(1, 80, 'Low is good at graphs')
plt.setp(lines, color='r', linewidth=2.0)

plt.show()