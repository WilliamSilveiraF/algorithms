while True:
    try:
        anHora, anMinuto = map(int, input().split(' '))
        hora = 0
        minuto = 0

        while anHora >= 30:
            hora += 1
            anHora -= 30
        while anMinuto >= 6:
            minuto += 1
            anMinuto -= 6
        if hora < 10 and minuto < 10:
            print("0"+ str(hora) + ":0" + str(minuto))
        elif hora >= 10 and minuto < 10:
            print(str(hora) + ":0" + str(minuto))
        elif hora < 10 and minuto >= 10:
            print("0" + str(hora) + ":" + str(minuto))
        else:
            print(str(hora) + ":" + str(minuto))
    except EOFError:
        break