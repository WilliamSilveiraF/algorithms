def sumAll(arr):
    res = 0
    for n in arr:
        res += n
    return res

def areAllZeros(arr):
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        return True
    else:
        return False

def areAllNonZero(arr):
    if arr[0] != 0 and arr[1] != 0 and arr[2] != 0:
        return True
    else:
        return False


matrix = [None] * 3

objSum = 0
objIsUndefined = True
totalMatrixValue = 0
zeroAmount = 0

for idx in range(3):
    matrix[idx] = list(map(int, input().split()))
    totalMatrixValue += sumAll(matrix[idx])
    zeroAmount += matrix[idx].count(0)

for line in matrix:
    if areAllZeros(line):
        objIsUndefined = False
        objSum = totalMatrixValue // 2
        break
    elif areAllNonZero(line):
        objIsUndefined = False
        objSum = sumAll(line)
        break


column1 = [matrix[0][0], matrix[1][0], matrix[2][0]]
column2 = [matrix[0][1], matrix[1][1], matrix[2][1]]
column3 = [matrix[0][2], matrix[1][2], matrix[2][2]]
diagonalA = [matrix[0][0], matrix[1][1], matrix[2][2]]
diagonalB = [matrix[0][2], matrix[1][1], matrix[2][0]]
if (areAllZeros(column1) or areAllZeros(column2) or areAllZeros(column3) or areAllZeros(diagonalA) or areAllZeros(diagonalB)) and objIsUndefined:
    objIsUndefined = False
    objSum = totalMatrixValue // 2

if objIsUndefined:
    if areAllNonZero(column1):
        objIsUndefined = False
        objSum = sumAll(column1)
    elif areAllNonZero(column2):
        objIsUndefined = False
        objSum = sumAll(column2)
    elif areAllNonZero(column3):
        objIsUndefined = False
        objSum = sumAll(column3)
    elif areAllNonZero(diagonalA):
        objIsUndefined = False
        objSum = sumAll(diagonalA)
    elif areAllNonZero(diagonalB):
        objIsUndefined = False
        objSum = sumAll(diagonalB)

for zero in range(zeroAmount):
    for line in range(3):
        for column in range(3):
            if matrix[line][column] == 0:
                matrix[line][column] = objSum - sumAll(matrix[line])
                if sumAll(matrix[line]) == objSum:
                    if areAllNonZero(matrix[line]):
                        continue
                    matrix[line][column] = 0
                matrix[line][column] = objSum - sumAll([matrix[0][column], matrix[1][column], matrix[2][column]])
                if sumAll([matrix[0][column], matrix[1][column], matrix[2][column]]) == objSum:
                    if areAllNonZero([matrix[0][column], matrix[1][column], matrix[2][column]]):
                        continue
for line in matrix:
    print(f"{line[0]} {line[1]} {line[2]}")
