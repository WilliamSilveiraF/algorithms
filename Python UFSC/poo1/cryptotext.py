nTurns = int(input())

for x in range(nTurns):
    result = ''
    word = input()[::-1]
    for letter in word:
        if letter.islower():
            result += letter
    print(result)
