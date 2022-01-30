irregularTurns, turns = map(int, input().split(' '))

irregulars = []

def isConsonant(letter):
    return not(letter in 'aeiou')

def isIrregular(singular):
    for pair in irregulars:
        if pair[0] == singular:
            return [True, pair[1]]
    return [False, '']

def endsInY(singular):
    penultimate = singular[len(singular) - 2]
    return len(singular) >= 2 and isConsonant(penultimate) and singular[-1] == 'y'

def endsInOSCHSHX(singular):
    ends = ["o", "s", "ch", "sh", "x"]
    for end in ends:
        if singular.endswith(end):
            return True
    return False

for turn in range(irregularTurns):
    singular, plural = input().split(' ')
    irregulars.append([singular, plural])

for turn in range(turns):
    word = input()
    if isIrregular(word)[0]:
        print(isIrregular(word)[1])
    elif endsInY(word):
        word = word[:-1] + 'ies'
        print(word)
    elif endsInOSCHSHX(word):
        word = word + 'es'
        print(word)
    else:
        word += 's'
        print(word)
