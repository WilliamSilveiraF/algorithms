a, b, c = list(map(int, input().split(' ')))
if a < b + c and b < a + c and c < a + b:
    print('Sou triângulo')
else:
    print('Não sou triângulo')