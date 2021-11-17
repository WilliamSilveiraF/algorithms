peso, altura = map(float, input('Digite seu peso e altura: ').split(' '))
imc = peso / altura**2
if imc < 18.5:
    print('Abaixo do Peso!')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade!')
else:
    pritn('Obesidade mórbida')
print('{}, {}'.format(peso, altura))
