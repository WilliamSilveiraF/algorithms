times = int(input())

for n in range(times):
    x1, y1, x2, y2, x3, y3 = (int(x) for x in input().split())
    ab = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    bc = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
    ac = ((x3 - x1)**2 + (y3 - y1)**2)**0.5

    sP = (ac + bc + ab) / 2

    area = (sP * (sP - ac) * (sP - bc) * (sP - ab))**0.5

    print(f"{area:.3f}")