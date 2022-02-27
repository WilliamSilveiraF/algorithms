diametro = int(input())
altura, largura, profundidade = map(int, input().split(' '))
volume = altura * largura * profundidade

if altura >= diametro and largura >= diametro and profundidade >= diametro and diametro**3 <= volume:
    print('S')
else:
    print('N')