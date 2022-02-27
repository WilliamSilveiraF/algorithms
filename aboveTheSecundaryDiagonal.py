choice = input()
matrix = [None] * 12
result = 0

for line in range(12):
    matrix[line] = [None] * 12

for line in range(12):
    for column in range(12):
        matrix[line][column] = float(input())

if choice == "S":
    for line in range(11):
        for column in range(11 - line):
            result += matrix[line][column]
elif choice == "M":
    for line in range(11):
        for column in range(11 - line):
            result += matrix[line][column] / 66

print("{:.1f}".format(result))
