myCash = float(input('Quanto você tem na carteira em reais? '))
dolar = 3.27
canBuy = myCash / dolar

print('Com o dólar no valor de {}, você pode comprar {} dólares com {} reais.'.format(dolar, canBuy, myCash))