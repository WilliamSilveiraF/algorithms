cases = int(input()) # pegue a quantidade dos meus inputs

for _ in range(cases):
    total = 0 # zere meu total para cada zero
    sequence = list(map(int, input().split())) #pegue a sequência de extensões

    for idx, options in enumerate(sequence):
        if idx == 0: #se for meu primeiro índice na sequência puler, poque ele representa a quantida de extensões na sequência
            continue
        if idx == sequence[0]: #se chega na última extensão some ela do valor inteiro, pois não vem mais nenhuma extensão após dela
            total += options
        else:
            total += options - 1 #do contrário sempre vai ter uma nova extensão em sequência conectada necessitando diminuir -1
    print(total)
