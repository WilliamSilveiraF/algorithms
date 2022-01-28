times = int(input())


def countSegments(myDigit):
    if myDigit == 0 or myDigit == 6 or myDigit == 9:
        return 6
    elif myDigit == 2 or myDigit == 3 or myDigit == 5:
        return 5
    elif myDigit == 4:
        return 4
    elif myDigit == 7:
        return 3
    elif myDigit == 8:
        return 7
    elif myDigit == 1:
        return 2
    else:
        return 'err'


for n in range(0, times):
    theNum = str(input())
    count = 0
    for digitIndex in range(0, len(theNum)):
        count += countSegments(int(theNum[digitIndex]))
    print(f'{count} leds')
