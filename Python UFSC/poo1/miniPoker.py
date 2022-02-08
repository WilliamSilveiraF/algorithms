cases = int(input())

def isSequence(arr):
    arr.sort()
    sequence = True
    for n in range(1, len(arr)):
        if arr[n] - arr[n - 1] != 1:
            sequence = False
    if sequence:
        return 200 + arr[0]
    else:
        return 0

def isFour(arr):
    if arr.count(arr[0]) == 4:
        return 180 + arr[0]
    elif arr.count(arr[1]) == 4:
        return 180 + arr[1]
    else:
        return 0

def isFullhouse(arr):
    myKeys = list(set(arr))
    amtCard1 = arr.count(myKeys[0])
    amtCard2 = arr.count(myKeys[1])
    if amtCard1 == 3 and amtCard2 == 2:
        return 160 + myKeys[0]
    elif amtCard1 == 2 and amtCard2 == 3:
        return 160 + myKeys[1]
    else:
        return 0
    print(myKeys)
print(isFullhouse([1, 1, 1, 10, 1]))

for case in range(cases):
    cards = list(map(int, input().split()))
