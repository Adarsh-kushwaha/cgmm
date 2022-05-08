import matplotlib.pyplot as plt

xcord = []
ycord = []


def drawLine(x1, y1, x2, y2):
    dy = y2-y1
    dx = x2-x1
    m = dy/dx
    p = 2*dy-dx
    x = x1
    y = y1

    if(m < 1):
        for x in range(x1, x2+1):
            if(p < 0):
                x = x+1
                xcord.append(x)
                ycord.append(y)
                p = p+2*dy

            else:
                x = x+1
                y = y + 1
                xcord.append(x)
                ycord.append(y)
                p = p+2*dy - 2*dx

    else:
        for x in range(y1, y2+1):
            if(p < 0):
                y = y+1
                xcord.append(x)
                ycord.append(y)
                p = p+2*dx
            else:
                x = x+1
                y = y + 1
                xcord.append(x)
                ycord.append(y)
                p = p+2*dx - 2*dy


drawLine(1, 1, 5, 3)

print(xcord, ycord)

plt.xlim(0, 10)
plt.ylim(0, 10)
plt.plot(xcord, ycord, "*")
plt.show()
