while True:
    try:
        lines, columns = map(int, input().split())
    except EOFError:
        break
    matrix = []

    startLine = 0
    startColumn = 0
    endLine = 0
    endColumn = 0

    for idx in range(lines):
        line = list(map(int, input().split()))

        if 1 in line:
            startLine = idx
            startColumn = line.index(1)
        if 2 in line:
            endLine = idx
            endColumn = line.index(2)
        matrix.append(line)
    print(abs(endColumn - startColumn) + abs(endLine - startLine))