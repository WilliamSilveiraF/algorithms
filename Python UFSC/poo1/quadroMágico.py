def sumAll(arr):
    res = 0
    for n in arr:
        res += n
    return res

matrix = [None] * 3

objSum = 0

for idx in range(3):
    matrix[idx] = list(map(int, input().split()))
    if objSum == 0 and not(0 in matrix[idx]):
        objSum = sumAll(matrix[idx])

diagonalA = [matrix[0][0], matrix[1][1], matrix[2][2]]
diagonalB = [matrix[0][2], matrix[1][1], matrix[2][0]]

if not(0 in matrix[0]):
    objSum = sumAll(matrix[0])
elif not(0 in matrix[1]):
    objSum = sumAll(matrix[1])
elif not(0 in matrix[2]):
    objSum = sumAll(matrix[2])
elif not(0 in diagonalA):
    objSum = sumAll(diagonalA)
elif not(0 in diagonalB):
    objSum = sumAll(diagonalB)

for idx, line in enumerate(matrix):
    if sumAll(line) != objSum:
        if line.count(0) == 3:
            for nIdx in range(len(matrix)):
                matrix[idx][nIdx] = objSum / 3
        elif line.count(0) == 2:
            for nIdx in range(len(matrix)):
                if matrix[idx][nIdx] == 0:
                    matrix[idx][nIdx] = objSum / 3
        else:
            nIdx = line.index(0)
            matrix[idx][nIdx] = objSum - sumAll(line)
    print(f"{matrix[idx][0]} {matrix[idx][1]} {matrix[idx][2]}")
