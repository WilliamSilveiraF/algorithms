nRooms = int(input())
rooms = list(map(int, input().split()))

maxValue = -100
totalSum = 0

for n in rooms:
    totalSum += n
    if maxValue < totalSum:
        maxValue = totalSum
    if totalSum < 0:
        totalSum = 0
print(maxValue)
