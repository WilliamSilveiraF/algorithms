while True:
    try:
        phrase = list(input())

        for idx in range(1, len(phrase)):
            letter = phrase[idx]
            beforeLetter = phrase[idx - 1]
            if beforeLetter == ' ' and (letter == ',' or letter == '.'):
                phrase[idx - 1] = ''

        result = ''
        for l in phrase:
            result += l
        print(result)
    except EOFError:
        break;
