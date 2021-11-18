while True:
    try:
        month, day = map(int, input().split(' '))
        qtDay = 0
        month -= 1
        while month > 0:
            if month == 2:
                qtDay += 29
                month -= 1
            elif month == 4 or month == 6 or month == 9 or month == 11:
                qtDay += 30
                month -= 1
            else:
                qtDay += 31
                month -= 1
        qtDay += day

        if qtDay == 359:
            print('E vespera de natal!')
        elif qtDay < 360:
            print('Faltam {} dias para o natal!'.format(360 - qtDay))
        elif qtDay == 360:
            print('E natal!')
        elif qtDay > 360:
            print('Ja passou!')
            continue
    except EOFError:
        break