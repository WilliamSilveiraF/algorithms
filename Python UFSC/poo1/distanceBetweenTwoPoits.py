x1, y1 = list(map(float, input().split(' ')))
x2, y2 = list(map(float, input().split(' ')))

diffDeXQuad = (x2 - x1)**2
diffDeYQuad = (y2 - y1)**2
res = (diffDeXQuad + diffDeYQuad)**(1/2)
print('{:.4f}'.format(res))
