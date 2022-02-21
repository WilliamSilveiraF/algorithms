choice = input()
result = 0
matrix = [None] * 12

for line in range(12):
    matrix[line] = [None] * 12

for line in range(12):
    for column in range(12):
        matrix[line][column] = float(input())

if choice == "S":
    for line in range(5):
        for column in range(line + 1, 11 - line):
            result += matrix[line][column]
elif choice == "M":
    for line in range(5):
        for column in range(line + 1, 11 - line):
            result += matrix[line][column] / 30

print("{:.1f}".format(result))
