import numpy as np
import pylab as pl

# Make an array of x values
x1 = [2, 15, 20, 5, 30, 26, 60]

# Make an array of y values for each x value
y1 = [1, 5, 10, 18, 20, 25, 27]

# Make an array of x values
x2 = [3, 20, 46, 15, 9, 30, 50, 62]

# Make an array of y values for each x value
y2 = [2, 6, 11, 20, 22, 26, 25, 30]

# Set new axis limits
pl.axis([0, 65, 0, 65])

# Show plot to plot x and y as red circles
pl.plot(x1, y1, 'b-', x2, y2, 'ro')

# Show the plot on the screen
pl.show()