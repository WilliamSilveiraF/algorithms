alternatives = ['A', 'B', 'C', 'D', 'E']

def isBlack(option):
    return int(option) <= 127

while True:
    turns = int(input())
    if turns == 0: break
    for turn in range(turns):
        options = input().split(' ')
        optionsMarked = 0
        for index, option in enumerate(options):
            if isBlack(option):
                optionsMarked += 1
                answer = index
        if optionsMarked == 1:
            print(alternatives[answer])
        else:
            print("*")
