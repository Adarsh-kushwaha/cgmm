# DDA for slope less than 1  m<1

from math import ceil
import matplotlib.pyplot as plt

xcord = []
ycord = []


def drawLine(x1, y1, x2, y2):
    dy = y2-y1
    dx = x2-x1
    m = dy/dx
    x = x1
    y = y1

    if(m < 1):
        for x in range(x1, x2+1):
            x += x1+1
            y = round(y+m)
            xcord.append(x)
            ycord.append(y)
            


drawLine(1, 1, 4, 3)

print(xcord, ycord)

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.plot(xcord, ycord, "*")
plt.show()
