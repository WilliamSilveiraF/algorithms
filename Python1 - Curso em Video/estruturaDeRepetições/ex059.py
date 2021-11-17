n1, n2 = map(int, input('Selecione dois números: ').split(' '))
print('Pressione:'
      '\n[1] Somar'
      '\n[2] Multiplicar'
      '\n[3] Maior'
      '\n[4] Novos números'
      '\n[5] Sair do programa')
choice = 0
choice = int(input('Selicione uma operação: '))
while choice != 5:

    if choice == 1:
        print('A soma entre {} e {} é igual: {}'.format(n1, n2, n1 + n2))
    elif choice == 2:
        print('A multiplicação entre {} e {} é igual: {}'.format(n1, n2, n1 * n2))
    elif choice == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior número é: {}'.format(n1, n2, maior))
    elif choice == 4:
        n1, n2 = map(int, input('Selecione dois novos números: ').split(' '))
    choice = int(input('Selicione uma nova operação: '))
print('Operação Finalizada')