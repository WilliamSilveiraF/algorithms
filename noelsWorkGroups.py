cases = int(input())
b = 0
a = 0
m = 0
d = 0
for _ in range(cases):
    _, tp, amt = input().split()

    if tp == "bonecos":
        b += int(amt)
    elif tp == "arquitetos":
        a += int(amt)
    elif tp == "musicos":
        m += int(amt)
    elif tp == "desenhistas":
        d += int(amt)

print(b // 8 + a // 4 + m // 6 + d // 12)

