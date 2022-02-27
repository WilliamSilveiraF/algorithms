theLine = int(input())
choice = input()
result = 0
matrix = [None] * 12

for line in range(12):
    matrix[line] = [None] * 12

for line in range(12):
    for column in range(12):
        matrix[line][column] = float(input())

if choice == "S":
    for column in range(12):
        result += matrix[theLine][column]
elif choice == "M":
    for column in range(12):
        result += matrix[theLine][column] / 12

print("{:.1f}".format(result))