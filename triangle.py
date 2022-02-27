a, b, c = list(map(float, input().split(' ')))
if a < b + c and b < a + c and c < a + b:
    print('Perimetro = {:.1f}'.format(a + b + c))
else:
    trapezio = ((a + b) * c) / 2
    print('Area = {}'.format(trapezio))