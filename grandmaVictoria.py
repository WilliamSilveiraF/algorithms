qtdVezes = 0
while True:
    vezes = int(input())
    qtdVezes += 1
    if vezes == 0:
        break

    print("Teste {}".format(qtdVezes))

    j, z = 0, 0
    for i in range(vezes):
        jDeposito, zDeposito = map(int, input().split(' '))
        j += jDeposito
        z += zDeposito
        print(j - z)
    print("")
