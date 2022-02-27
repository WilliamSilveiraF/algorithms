citizens = int(input())
answers = input().split(' ')
okAmount = 0
for answer in answers:
    if answer == '0':
        okAmount += 1

print('Y') if okAmount / citizens * 100 > 50 else print('N')
