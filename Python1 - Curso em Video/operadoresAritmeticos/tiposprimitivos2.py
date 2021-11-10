algo = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(algo)))
print('É um número? {}'.format(algo.isnumeric()))
print('É alfabético? {}'.format(algo.isalpha()))
print('É alfanumérico? {}'.format(algo.isalnum()))
print('Todas as letras são maiúsculas? {}'.format(algo.isupper()))
print('Todas as letras são minúsculas? {}'.format(algo.islower()))
print('Está capitalizada? {}'.format(algo.istitle()))