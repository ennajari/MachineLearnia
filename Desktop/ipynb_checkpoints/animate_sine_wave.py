import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generate x data
x = np.linspace(0, 2 * np.pi, 100)

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot(x, np.sin(x))

# Set the title and labels
ax.set_title("Animated Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")

# Initialization function
def init():
    line.set_ydata(np.sin(x))
    return line,

# Animation function
def animate(i):
    line.set_ydata(np.sin(x + i / 10.0))  # Update the y data
    return line,

# Call the animator
anim = FuncAnimation(fig, animate, init_func=init, frames=100, interval=100, blit=True)

# Display the plot in an interactive window
plt.show()

