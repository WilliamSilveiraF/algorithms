posiçao = 0
maior = 0

for q in range(0, 100):
    num = int(input())
    if maior < num:
        maior = num
        posiçao = q + 1
print(maior)
print(posiçao)