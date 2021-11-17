print('Digite 0 se à vista com 10% de desconto\n'
      'Digite 1 se à vista no cartão com 5% de desconto\n'
      'Digite 2 em até 2x no cartão com preço normal\n'
      'Digite 3 se 3x ou mais com 20% de Juros')

myChoice = int(input('Qual a forma de pagamento: '))
myPrice = float(input('Qual o valor do produto:'))
if myChoice == 0:
    valueAPagar = myPrice * 0.9
elif myChoice == 1:
    valueAPagar = myPrice * 0.95
elif myChoice == 2:
    valueAPagar = myPrice
elif myChoice == 3:
    valueAPagar = myPrice * 1.20
else:
    print('Escolha inválida')
print('Valor a pagar R$ {:.2f}'.format(valueAPagar))