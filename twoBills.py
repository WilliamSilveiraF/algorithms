bills = [100, 50, 20, 10, 5, 2] #Ordena as notas de forma decrescente para facilitar a exclusão

while True:
    isPossible = False #Minha flag para quando descrobrir que é possível a soma de 2 notas darem o troco
    value, payment = map(int, input().split()) #pegar o valor e o pagamento

    if value == 0 and payment == 0: #se eles forem zero é para quebrar o loop conforme meu enuciado
        break
    diff = payment - value #pego o valor total do meu troco

    for idx, note in enumerate(bills): #Os 2 loops foram organizado de forma que excluí notas já analisadas ou iguais
        for nIdx, note2 in enumerate(bills):
            if nIdx <= idx:
                continue
            if note + note2 == diff: #testando se a soma dos dois números dá o valor exato do troco
                isPossible = True #se sim aciona minha flag e quebro o primeiro o loop
                break
        if isPossible: # com minha flag ativada, quebro o outro loop e printo que é possível
            print("possible")
            break
    if not isPossible: #se eu terminar meus 2 loop que fazem a combinação das notas e a minha Flag ainda é False, ela vai print que é impossível
        print("impossible")
