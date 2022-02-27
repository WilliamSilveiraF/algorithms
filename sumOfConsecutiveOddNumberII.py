n = int(input())
for x in range(0, n):
    x, y = map(int, input().split(' '))
    if x > y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x
    soma = 0
    for num in range(menor + 1, maior):
        if num % 2 != 0:
            soma += num
    print(soma)