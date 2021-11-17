num = int(input('Digite um número: '))
contadorDivisivel = 0
for x in range(1, num+1):
    if num % x == 0:
        contadorDivisivel += 1
if contadorDivisivel == 2:
    print('É primo')
else:
    print('Não é primo')