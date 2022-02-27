qtd = int(input())
somatorio = 0
for x in range(qtd):
    l, c = map(int, input().split(' '))
    if l > c:
        somatorio += c
print(somatorio)
