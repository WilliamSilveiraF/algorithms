anoDeNascimento = int(input('Qual seu ano de Nascimento: '))
idade = 2021 - anoDeNascimento
if idade < 18:
    print('Você ainda vai se alistar no exército!')
    print('Faltam {} ano(s) para seu alistamento'.format(18 - idade))
elif idade == 18:
    print('É hora do alistamente no exército!')
else:
    print('Você passou do tempo de alistamento! Compareça com urgência na junta militar mais próxima.')
    print('Há {} ano(s) em situação irregular!'.format(idade - 18))