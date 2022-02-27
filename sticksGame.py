while True:
    turns = int(input())
    if turns == 0: break
    canTurnRectangle = 0

    for turn in range(turns):
        stickSize, amount = map(int, input().split(' '))

        if amount % 2 != 0:
            amount -= 1
        canTurnRectangle += amount
    rectangles = canTurnRectangle // 4
    print(rectangles)
