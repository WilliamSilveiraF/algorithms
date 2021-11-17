n1, n2, n3, n4, n5, n6 = map(int, input('Digite seis números: ').split(' '))
myArr = [n1, n2, n3, n4, n5, n6]

soma = 0
for x in range(0, len(myArr)):
    if myArr[x] % 2 == 0:
        soma = soma + myArr[x]
print(soma)