sexo = str(input('Digite seu sexo: '))

while not (sexo in 'MmFf'):
    sexo = str(input('Digite seu sexo: '))
print('Fim, seu sexo é {}'.format(sexo.upper()))