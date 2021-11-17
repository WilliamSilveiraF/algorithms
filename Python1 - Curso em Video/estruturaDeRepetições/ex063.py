#Fibonacci
n = int(input('Quantos termos você quer mostrar: '))
p1 = 0
p2 = 1
print('{} -> {}'.format(p1, p2), end='')
cont = 3
while cont <= n:
    p3 = p1 + p2
    print(' -> {}'.format(p3), end='')
    p1 = p2
    p2 = p3
    cont += 1
print(' -> FIM')