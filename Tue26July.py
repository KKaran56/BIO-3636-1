# 26 July 2022

# Making plots with matplotlib.
from matplotlib import pyplot as plt

# plt.savefig("XXX.tiff") is used to save the matplotlib figure.

x = [2, 3, 4]
y = [3, 5, 9]
plt.plot(x ,y)
plt.show()
plt.savefig("mm.jpg")

# scatter() is used to make a scatter plot.

plt.scatter(x ,y)

# Box plots are better than bars because with much less ink, boxplots show us a lot of information.

# Function to create a boxplot.

plt.boxplot(x)

# Histgrams give us the frequency distribution. 

plt.hist()

# Sometimes we need multiple plots.

fig, ax = plt.subplots(rows = 1, cols = 3)
ax[0].plot(x, y)
ax[1].plot(x1, y1)
ax[2].plot(x2, y2)

# You can superimpose a scatter plot on box plot by adding some random noise to the scatter plot.

# There is another plot called a violin plot. It is a good idea to be cautious when using such plots because they produce a lot of smoothening, which only makes
# sense when there is a large data set.

