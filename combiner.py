turns = int(input())

for turn in range(turns):
    myResult = ''
    frstWord, scndWord = str(input()).split(' ')
    greaterWord = len(frstWord if len(frstWord) > len(scndWord) else scndWord)
    for n in range(greaterWord):
        if len(frstWord) > n:
            myResult += frstWord[n]
        if len(scndWord) > n:
            myResult += scndWord[n]
    print(myResult)
