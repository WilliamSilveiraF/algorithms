letter = input()
phrase = input().split(' ')
hasTheLetter = 0

for word in phrase:
    if letter in word:
        hasTheLetter += 1

print(f'{hasTheLetter / len(phrase) * 100:.1f}')
