words = input().split(' ')
result = ''
for word in words:
    formatedWord = ''
    for index, letter in enumerate(word):
        if index % 2 != 0:
            formatedWord += letter
    result += formatedWord + ' '
mySlice = slice(0, len(result) - 1)
print(result[mySlice])