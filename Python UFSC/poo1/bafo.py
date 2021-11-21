amountVez = 1
while True:
    vezes = int(input())
    if vezes == 0:
        break

    amountA = 0
    amountB = 0
    for vez in range(vezes):
        a, b = map(int, input().split(' '))
        amountA += a
        amountB += b
    print(f"Teste {amountVez}")
    if amountA > amountB:
        print("Aldo")
    else:
        print("Beto")
    print(" ")
    amountVez += 1