number = int(input('Escolha um número: '))
print('Pressione:\n'
      '0 -> conversão em Binário\n'
      '1 -> conversão em Octal\n'
      '2 -> conversão em Hexadecimal')
conversao = int(input('\nEscolha um método de conversão: '))
if conversao == 0:
    print('{} em binário é {}'.format(number, bin(number)[2:]))
elif conversao == 1:
    print('{} em octal é {}'.format(number, oct(number)[2:]))
elif conversao == 2:
    print('{} em hexadecimal é {}'.format(number, hex(number)[2:]))