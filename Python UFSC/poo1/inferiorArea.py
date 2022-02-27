choice = input()
matrix = [None] * 12
result = 0

for line in range(12):
    matrix[line] = [None] * 12

for line in range(12):
    for column in range(12):
        matrix[line][column] = float(input())

for line in range(7, 12):
    for column in range(12 - line, line):
        result = result + matrix[line][column]
if choice == "M":
        result = result / 30

print(f"{result:.1f}")
