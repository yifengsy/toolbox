## This snippet demonstrates how to generate a sample plot using matplotlib

import matplotlib.pyplot as plt

my_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_y = [1, 4, 9, 16, 25, 36, 59, 64, 81, 100]

plt.scatter(my_x, my_y)

plt.xlabel("My X Label")
plt.ylabel("My Y Label")

plt.show()

