import math

def getSide(iX, iY, fX, fY):
    size = math.sqrt(pow((iY-fY), 2) + pow((iX-fX), 2))
    return size
def getArea(side1, side2, side3, side4, diagonal1, diagonal2):
    s = (side1 + side2 + side3 + side4) / 2
    t = (s - side1) * (s - side2) * (s - side3) * (s - side4) - ((1 / 4) * (side1 * side3 + side2 * side4 + diagonal2 * diagonal1) * (side1 * side3 + side2 * side4 - diagonal2 * diagonal1))
    return math.sqrt(t)

coordA = []
coordB = []

for _ in range(4):
    coordA.append(list(map(int, input().split())))
for _ in range(4):
    coordB.append(list(map(int, input().split())))

sidesA = []
for nowSide in range(0, len(coordA)):
    side = getSide(coordA[nowSide - 1][0], coordA[nowSide - 1][1], coordA[nowSide][0], coordA[nowSide][1])
    sidesA.append(side)
sidesA.append(getSide(coordA[0][0], coordA[0][1], coordA[2][0], coordA[2][1]))
sidesA.append(getSide(coordA[1][0], coordA[1][1], coordA[3][0], coordA[3][1]))

sidesB = []
for nowSide in range(0, len(coordB)):
    side = getSide(coordB[nowSide - 1][0], coordB[nowSide - 1][1], coordB[nowSide][0], coordB[nowSide][1])
    sidesB.append(side)
sidesB.append(getSide(coordB[0][0], coordB[0][1], coordB[2][0], coordB[2][1]))
sidesB.append(getSide(coordB[1][0], coordB[1][1], coordB[3][0], coordB[3][1]))

tA = getArea(sidesA[0], sidesA[1], sidesA[2], sidesA[3], sidesA[4], sidesA[5])
tB = getArea(sidesB[0], sidesB[1], sidesB[2], sidesB[3], sidesB[4], sidesB[5])

print("terreno A") if tA > tB else print("terreno B")