myKeyboard = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'

while True:
    try:
        myStr = input()
        myResult = ''
        for myLetter in range(len(myStr)):
            if myStr[myLetter] == ' ':
                myResult += ' '
                continue
            letterIndex = myKeyboard.find(myStr[myLetter])
            myResult += myKeyboard[letterIndex - 1]
        print(myResult)
    except EOFError:
        break
