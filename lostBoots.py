right = [None] * 61
left = [None] * 61

while True:
    try:
        turns = int(input())

        for nSize in range(30, 61):
            right[nSize] = 0
            left[nSize] = 0

        for _ in range(turns):
            size, side = input().split(' ')
            if side == 'D':
                right[int(size)] += 1
            else:
                left[int(size)] += 1
        pairsAmount = 0
        for sSize in range(30, 61):
            if right[sSize] < left[sSize]:
                pairsAmount += right[sSize]
            else:
                pairsAmount += left[sSize]
        print(pairsAmount)
    except EOFError:
        break