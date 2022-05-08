# Python3 program for implementing
# Mid-Point Ellipse Drawing Algorithm

import matplotlib.pyplot as plt

xcord = []
ycord = []


def midptellipse(rx, ry,):

    x = 0
    y = ry

    # Initial decision parameter of region 1
    d1 = ((ry * ry) - (rx * rx * ry) +
          (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    # For region 1
    while (dx < dy):
        # Checking and updating value of
        # decision parameter based on algorithm
        if (d1 < 0):
            x += 1
            xcord.append(x)
            ycord.append(y)
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            xcord.append(x)
            ycord.append(y)
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

    # Decision parameter of region 2
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) +
          ((rx * rx) * ((y - 1) * (y - 1))) -
          (rx * rx * ry * ry))

    # Plotting points of region 2
    while (y >= 0):

        # Checking and updating parameter
        # value based on algorithm
        if (d2 > 0):
            y -= 1
            xcord.append(x)
            ycord.append(y)
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            xcord.append(x)
            ycord.append(y)
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)

# Driver code


# To draw a ellipse of major and
# minor radius 15, 10 centered at (50, 50)
midptellipse(5, 10)
print(xcord, ycord)

plt.xlim(0, 50)
plt.ylim(0, 50)
plt.plot(xcord, ycord, "*")
plt.show()

# This code is contributed by chandan_jnu
