import math

adjacente, oposto = list(map(int, input().split(' ')))

somaDeCatetos = adjacente**2 + oposto**2
print('A hipotenusa é {}'.format(math.sqrt(somaDeCatetos)))
