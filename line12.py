import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
lines = plt.plot(t, t, 'b-', linewidth=2.0, label='Thing 1')
lines = plt.plot(t, t**2, 'r-', linewidth=2.0, label='Thing 2')
lines = plt.plot(t, t**3, 'g-', linewidth=2.0, label='Thing 3')

plt.xlabel('Dummy data for x')
plt.ylabel('Dummy data for y')
plt.title('An example graph')

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()