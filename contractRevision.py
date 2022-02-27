while True:
    myResult = ''
    myDigit, myValue = map(str, input('').split(' '))
    if myDigit == "0" and myValue == "0":
        break
    for aDigit in myValue:
        if aDigit != myDigit:
            myResult += aDigit
    if myResult == '':
        myResult = '0'
    print(int(myResult))
