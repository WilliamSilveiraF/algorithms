while True:
    try:
        lines, _ = map(int, input().split()) #quantas linhas são a matriz

        saca = 0
        litro = 0
        for _ in range(lines): #leia todas as linhas
            line = list(map(int, input().split()))
            for x in line:
                litro += x #e soma todos os valores de cada linha e pega quantos litros totais

        while litro >= 60: #transforma se a quantidade de litros maior do que 60 em saca
            litro -= 60
            saca += 1

        print(f"{saca} saca(s) e {litro} litro(s)")
    except EOFError:
        break