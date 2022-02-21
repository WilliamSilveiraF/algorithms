choice = input()
matrix = [None] * 12
result = 0

for line in range(12):
    matrix[line] = [None] * 12

for line in range(12):
    for column in range(12):
        matrix[line][column] = float(input())

if choice == "S":
    for line in range(7, 12):
        for column in range(12 - line, line):
            result += matrix[column][line]
elif choice == "M":
    for line in range(7, 12):
        for column in range(12 - line, line):
            result += matrix[column][line] / 30

print("{:.1f}".format(result))
