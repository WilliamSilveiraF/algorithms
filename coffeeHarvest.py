while True:
    try:
        lines, _ = map(int, input().split())

        saca = 0
        litro = 0
        for _ in range(lines):
            line = list(map(int, input().split()))
            for x in line:
                litro += x

        while litro >= 60:
            litro -= 60
            saca += 1

        print(f"{saca} saca(s) e {litro} litro(s)")
    except EOFError:
        break