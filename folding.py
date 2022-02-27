contador = 0
while True:
    entrada = int(input())

    if entrada == -1:
        break
    anterior = 2
    for i in range(0, entrada):
        anterior = anterior + 2**i

    contador += 1
    print('Teste {}'.format(contador))
    print(anterior**2)
    print('')