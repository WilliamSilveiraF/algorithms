state = True
vez = 0
while state:
    valor = int(input())
    if valor == 0:
        break
    vez += 1
    qCinq = 0
    qDez = 0
    qCinco = 0
    qUm = 0

    while valor >= 50:
        valor -= 50
        qCinq += 1
    while valor >= 10:
        valor -= 10
        qDez += 1
    while valor >= 5:
        valor -= 5
        qCinco += 1
    while valor >= 1:
        valor -= 1
        qUm += 1
    print('Teste {}\n{} {} {} {}'.format(vez, qCinq, qDez, qCinco, qUm))