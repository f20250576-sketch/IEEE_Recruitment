import numpy as np

import matplotlib.pyplot as plt

# Generate 1000 random numbers from a normal distribution
data = np.random.normal(loc=0, scale=1, size=1000)

# Create a scatter plot
plt.scatter(range(len(data)), data, alpha=0.6)
plt.title('Scatter Plot of 1000 Random Numbers from Normal Distribution')
plt.xlabel('Index')
plt.ylabel('Random Value')
plt.grid(True)
plt.show()