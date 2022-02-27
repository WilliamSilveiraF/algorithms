while True:
    lines, columns = map(int, input().split(' '))
    if lines == 0 and columns == 0:
        break

    result = 0
    case1 = True
    case2 = False
    case3 = True
    case4 = True
    matrix = []

    solved = [0] * columns

    for x in range(lines):
        newLine = list(map(int, input().split()))
        matrix.append(newLine)

    for line in matrix:
        if line.count(1) == columns:
            case1 = False
        if line.count(1) == 0:
            case4 = False
        for idx in range(columns):
            if solved[idx] == 0 and line[idx] == 1:
                solved[idx] = 1
    checklist = []
    for column in range(columns):
        for line in range(lines):
            checklist.append(matrix[line][column])
        if checklist.count(1) == lines:
            case3 = False
        checklist = []
    if solved.count(1) == columns:
        case2 = True

    if case1:
        result += 1
    if case2:
        result += 1
    if case3:
        result += 1
    if case4:
        result += 1
    print(result)
