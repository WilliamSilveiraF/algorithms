lines, columns = map(int, input().split())

isLadder = True
ref = -1

for idx in range(lines):
    line = list(map(int, input().split()))
    if isLadder:
        alreadyIncremented = False
        isDiffZero = False
        for cIdx, column in enumerate(line):
            if 0 != column:
                isDiffZero = True
                if ref >= cIdx:
                    isLadder = False
                break
            elif ref < cIdx and not(isDiffZero):
                ref += 1
                alreadyIncremented = True
        if not alreadyIncremented:
            ref += 1
print("S") if isLadder else print("N")
