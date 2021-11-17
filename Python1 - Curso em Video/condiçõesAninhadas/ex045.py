import random

print('Faça uma escolha:\n'
      '0: Pedra\n'
      '1: Papel\n'
      '2: Tesoura')

yourChoice = int(input('Sua escolha: '))
inteiro = random.randint(0, 2)

if (yourChoice == 0 and inteiro == 2):
    print('Você venceu!')
elif yourChoice == 1 and inteiro == 0:
    print('Você venceu!')
elif yourChoice == 2 and inteiro == 1:
    print('Você venceu!')
elif yourChoice == inteiro:
    print('Empatou :D')
else:
    print('Você perdeu!')



print(inteiro)