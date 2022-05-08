import matplotlib.pyplot as plt

xcord = []
ycord = []


def drawLine(x, y, r):
    x = 0
    y = r
    p = 1-r
    z = x >= y

    if(p < 0):
        for x in range(x, y):
            if(x <= y):
                if(p < 0):
                    x = x+1
                    y = y
                    xcord.append(x)
                    ycord.append(y)
                    p = p+2*x+1

                else:
                    x = x+1
                    y = y - 1
                    xcord.append(x)
                    ycord.append(y)
                    p = p+2*x+1-2*y+1
            else:
                break


drawLine(0, 0, 9)

print(xcord, ycord)

plt.xlim(0, 20)
plt.ylim(0, 20)
plt.plot(xcord, ycord, "*")
plt.show()
