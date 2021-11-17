num = int(input('Digite um número: '))
contador = 0
while num != 999:
    contador += num
    num = int(input('Digite um número: '))

print('Fim, a soma foi: {}'.format(contador))