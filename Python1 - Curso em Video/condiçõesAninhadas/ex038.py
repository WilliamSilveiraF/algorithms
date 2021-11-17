n1, n2 = input('Escreva os valores em ordem: ').split(' ')

if n1 > n2:
    print('O primeiro valor é maior')
elif n1 < n2:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')