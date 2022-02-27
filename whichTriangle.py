a, b, c = map(int, input().split())

squareAB = a**2 + b**2
squareAC = a**2 + c**2
squareBC = b**2 + c**2
if a < b + c and b < a + c and c < a + b:
    if a == b and a == c and b == c:
        print('Valido-Equilatero\nRetangulo: N')

    if (a == b and c != a) or (a == c and b != a) or (c == b and b != a):
        if squareAB == c**2 or squareAC == b**2 or squareBC == a**2:
            print(f'Valido-Isoceles\nRetangulo: S')
        else:
            print(f'Valido-Isoceles\nRetangulo: N')

    if a != b and b != c and a != c:
        if squareAB == c**2 or squareAC == b**2 or squareBC == a**2:
            print(f'Valido-Escaleno\nRetangulo: S')
        else:
            print(f'Valido-Escaleno\nRetangulo: N')
else:
    print('Invalido')