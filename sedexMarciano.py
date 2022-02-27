from math import sqrt
l, a, p, r = map(int, input().split())

if sqrt(l**2 + a**2 + p**2) <= 2*r:
    print("S")
else:
    print("N")