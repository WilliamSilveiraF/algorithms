jumpHeight, pipesNumber = map(int, input().split())
heights = list(map(int, input().split()))

for h in range(1, pipesNumber):
    if abs(heights[h - 1] - heights[h]) > jumpHeight:
        print("GAME OVER")
        break
    if h == len(heights) - 1:
        print('YOU WIN')
