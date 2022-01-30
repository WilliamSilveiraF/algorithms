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
        for n in range(myKeyBoots):


        print(myKeyBoots, right, left)
    except EOFError:
        break
