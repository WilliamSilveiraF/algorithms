#soma de todos os ímpares e múltiplos de 3
soma = 0
for x in range(1, 10):
    if x % 2 != 0 and x % 3 == 0:
        soma = soma + x
print(soma)