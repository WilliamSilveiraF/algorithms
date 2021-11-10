import math

num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {} arrendonda para cima'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {} arrendonda para baixo'.format(num, math.floor(raiz)))
