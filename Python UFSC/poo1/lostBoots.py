while True:
    try:
        times = int(input())
        right = []
        left = []
        result = 0
        for n in range(times):
            bootNumber, sideType = str(input()).split(' ')
            if sideType == 'D':
                right.append(bootNumber)
            else:
                left.append(bootNumber)
        myKeyBoots = list(dict.fromkeys(right))

        for p in myKeyBoots:
            leftPairs = left.count(myKeyBoots[int(p)])
            rightPairs = right.count(myKeyBoots[int(p)])
            if leftPairs > 0:
                equalsBoot = rightPairs if leftPairs > rightPairs else leftPairs
                result += equalsBoot
        print(result)
    except EOFError:
        break
