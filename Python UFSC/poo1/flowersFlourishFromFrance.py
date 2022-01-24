while True:
    myWords = input('').lower().split(' ')
    firstLetter = myWords[0][0]
    if firstLetter == "*":
        break

    for word in myWords:
        if word[0] != firstLetter:
            print('N')
            break
        if myWords[-1] == word:
            print('Y')
