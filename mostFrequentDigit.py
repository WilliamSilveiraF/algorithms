while True:
    try:
        numbers = {}  # crio um objeto para armazena cada número e sua respectiva frequência
        mostFrequent = (-1, -1) # cria uma tupla de controle de mais frequente (key, value)
        sequence = input() #pego minha sequencia
        for n in sequence: #armazeno todos os números no meu dicionário
            if n not in numbers.keys(): #se meu número ainda não existe no meu dicionário cadastre ele
                numbers[n] = 1
            else: #se ele já existe, some 1 relativo a frequência
                numbers[n] += 1
        for key, value in numbers.items(): #pegue o mais frequente
            mfKey, mfValue = mostFrequent #pega a tupla mais do mais frquente atual
            if value == mfValue: #se o valores forem iguais, pegue o qual o número é maior
                if int(key) > int(mfKey):
                    mostFrequent = (key, value)
            elif value > mfValue: #se o valor atual é mais frequente, atribua essa tupla para ele
                mostFrequent = (key, value)
        print(mostFrequent[0]) #print o número mais frequente
    except EOFError:
        break;
