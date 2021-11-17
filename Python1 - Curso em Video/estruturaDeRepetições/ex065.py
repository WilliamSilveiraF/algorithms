num = int(input('Digite um número: '))
choice = 'S'
soma = num
media = num
amount = 1
menor = num
maior = num
choice = input('Quer continuar: ').upper()
while choice == 'S':
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    amount += 1
    media = soma / amount
    choice = input('Quer continuar: ').upper()
print('\nA soma de todos os números digitados é {}'
      '\nA média foi: {}'
      '\nMaior número: {}'
      '\nMenor número: {}'.format(soma, media, maior, menor))