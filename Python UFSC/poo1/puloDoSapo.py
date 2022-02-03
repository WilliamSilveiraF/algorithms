amtStone, amtFrog = map(int, input().split(' '))
stones = [0] * (amtStone + 1)
for x in range(amtFrog):
    initPosition, jumpLength = map(int, input().split(' '))
    for p in range(initPosition, amtStone + 1, jumpLength):
        stones[p] = 1
    for p in range(initPosition, 0, -jumpLength):
        stones[p] = 1
for res in range(1, amtStone + 1):
    print(stones[res])
