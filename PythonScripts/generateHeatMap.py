import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.normal(0, 1, 500)
y = np.random.normal(0, 1, 500)

# Create a hexbin plot
plt.hexbin(x, y, gridsize=20, cmap='inferno', bins='log', mincnt=1)

# Add a colorbar
plt.colorbar()

# Set the axis labels and title
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Heatmap based on X-Y coordinates')

# Display the plot
plt.show()
