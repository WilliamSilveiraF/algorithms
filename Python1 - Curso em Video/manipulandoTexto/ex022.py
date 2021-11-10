frase = input()
maiuscula = frase.upper()
minuscula = frase.lower()
size = len(frase.replace(' ', ''))
sizeFirstName = len(frase.split(' ')[0])
print('Em maiúsculas: {}\n'
      'Em minúsculas: {}\n'
      'Número de letras: {}\n'
      'Número de letras do primeiro nome: {}'.format(maiuscula, minuscula, size, sizeFirstName))
