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


def isThree(arr):
    myKeys = list(set(arr))
    for n in myKeys:
        if arr.count(n) == 3:
            return 140 + n
    return 0


def isTwoPair(arr):
    myPair = []
    for x in arr:
        if arr.count(x) == 2 and x not in myPair:
            myPair.append(x)
    myPair.sort()
    if len(myPair) != 2:
        return 0
    else:
        return 20 + (myPair[-1] * 3) + (myPair[0] * 2)


def isPair(arr):
    for x in arr:
        if arr.count(x) == 2:
            return x
    return 0


for case in range(cases):
    result = 0
    cards = list(map(int, input().split()))
    if isSequence(cards):
        result = isSequence(cards)
    elif isFour(cards):
        result = isFour(cards)
    elif isFullhouse(cards):
        result = isFullhouse(cards)
    elif isThree(cards):
        result = isThree(cards)
    elif isTwoPair(cards):
        result = isTwoPair(cards)
    elif isPair(cards):
        result = isPair(cards)
    print(f"Teste {case + 1}\n"
          f"{result}\n")
