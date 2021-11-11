a, b, c = list(map(int, input().split(' ')))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('menor: {}\nmaior: {}'.format(menor, maior))