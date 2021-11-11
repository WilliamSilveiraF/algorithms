from random import randint
from time import sleep
numEscolhido = int(input())
numSorted = randint(0, 5)
print('Processando...')
sleep(2)
if numEscolhido == numSorted:
    print('Você acertou!!')
else:
    print('Você errou :(')
print(numSorted)
