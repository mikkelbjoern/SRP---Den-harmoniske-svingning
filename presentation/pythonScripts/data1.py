import random, math
from matplotlib import pyplot as plt

outputM = open("model1.plot","w")
outputM.write("t x(t)\n\n")
outputD = open("data.plot","w")
outputD.write("t x(t)\n\n")


def uncData(x):
    return random.gauss(x, 0.1)

pres = 1000
leng = 30*pres

data = []
dataT = []
k = 3.6
m=500
mu = 5
x = -5
dx = 0.001
ddx = 0
for i in range(leng):
    ddx = -( (k/m)*x + (dx)/(math.fabs(dx))* mu*(dx)**2)/pres
    dx += ddx
    x += dx
    if i%100 == 0:
        point = uncData(x)
        dataT.append(i/pres)
        data.append(point)
        outputD.write(str(i/pres) + " " + str(point) + "\n")


model = []
modelT = []

x = -5
dx = 0.001
ddx = 0
for i in range(leng):
    ddx = -( (k/m)*x)/pres
    dx += ddx
    x += dx
    modelT.append(i/pres)
    model.append(x)
    if i%50 == 0:
        outputM.write(str(i/pres) + " " + str(x) + "\n")





plt.plot(dataT,data, "ro")
plt.plot(modelT,model,"b")
plt.xlabel("Tid (s)")
plt.ylabel("Afvigelse af hviletilstand(cm)")

plt.show()
