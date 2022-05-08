import matplotlib.pyplot as plt

# x axis values
x = [1, 1, 1, 1, 2, 3, 3, 3, 3]
# corresponding y axis values
y = [4, 3, 2, 1, 1, 1, 2, 3, 4]

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.plot(x, y, "*")
plt.show()
