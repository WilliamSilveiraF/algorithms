tamanho = int(input('Qual o tamanho da sua viagem em Km? '))

if tamanho <= 200:
    preço = tamanho * 0.50
else:
    preço = tamanho * 0.45
print('Uma viagem de {}Km custa {}'.format(tamanho, preço))
