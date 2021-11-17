word = input('Digite uma palavra: ')
reverse = word[::-1]

if word == reverse:
    print('É palíndromo')
else:
    print('Não é palíndromo')
