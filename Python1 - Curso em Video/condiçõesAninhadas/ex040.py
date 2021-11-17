n1, n2 = map(float, input('Escreva suas notas: ').split(' '))
media = (n1 + n2) / 2
if media < 5.0:
    print('REPROVADO!')
elif media >= 5.0 and media < 7.0:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')