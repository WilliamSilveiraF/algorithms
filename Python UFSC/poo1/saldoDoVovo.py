vezes, saldo = map(int, input().split(' '))

historia = []
historia.append(saldo)
for vez in range(vezes):
    saldo += int(input())
    historia.append(saldo)

print(min(historia))