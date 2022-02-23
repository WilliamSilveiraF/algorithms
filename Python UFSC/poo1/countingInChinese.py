cases = int(input())

for _ in range(cases):
    matrixSize, nonNullInputs = map(int, input().split())
    matrix = [None] * matrixSize
    for line in range(matrixSize):
        matrix[line] = [None] * matrixSize