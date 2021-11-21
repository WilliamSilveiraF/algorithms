lado = int(input())
qtdVzs = 0
while lado >= 2:
    lado = lado / 2
    qtdVzs += 1
print(4**qtdVzs)