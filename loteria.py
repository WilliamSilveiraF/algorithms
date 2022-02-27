bets = list(map(int, input().split(' ')))
result = list(map(int, input().split(' ')))

right = 0
for bet in bets:
    if bet in result:
        right += 1

if right == 3:
    print("terno")
elif right == 4:
    print("quadra")
elif right == 5:
    print("quina")
elif right == 6:
    print("sena")
else:
    print("azar")