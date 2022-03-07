while True:
    cEPR = 0
    cEHD = 0
    cINTR = 0

    try:
        cases = int(input())

        for _ in range(cases):
            test = input().split()
            if "EPR" == test[1]:
                cEPR += 1
            elif "EHD" == test[1]:
                cEHD += 1
            else:
                cINTR += 1
        print(f"EPR: {cEPR}\n"
              f"EHD: {cEHD}\n"
              f"INTRUSOS: {cINTR}")
    except EOFError:
        break