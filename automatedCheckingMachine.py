sequence1 = input().split(' ')
sequence2 = input().split(' ')

for x in range(len(sequence1)):
    if sequence1[x] == sequence2[x]:
        print('N')
        break
    if x == len(sequence1) - 1:
        print('Y')
