n, k = map(int, input().split(' '))

towers = list(map(int, input().split(' ')))

pico = False
vale = False
qtdPicos = 0
qtdVales = 0

for i in range(1, n):
    if towers[i] > towers[i - 1] and not pico:
        pico = True
        vale = False
        qtdPicos += 1
    if towers[i] < towers[i - 1] and not vale:
        vale = True
        pico = False
        qtdVales += 1

if qtdVales == k and qtdPicos == k:
    print("beautiful")
else:
    print("ugly")
