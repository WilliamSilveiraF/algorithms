choice = input()

mat = [None] * 12

result = 0

for line in range(12):

    mat[line] = [None] * 12

for line in range(12):
    for column in range(12):
        mat[line][column] = float(input())

if choice == "S":
    for line in range(1, 12):
        for column in range(line):
            result += mat[line][column]
elif choice == "M":

    for line in range(1, 12):
        for column in range(line):
            result += mat[line][column] / 66

print("{:.1f}".format(result))
