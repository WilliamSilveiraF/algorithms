from math import ceil

while True:
    size = int(input())

    if size == 0:
        break

    for line in range(size):
        for column in range(size):
            myValue = ceil((size - abs(line - column) - abs(column + line - (size - 1))) / 2)
            space = ""
            if column == 0 or myValue > 9:
                space = "  "
            elif column <= size - 1:
                space = "   "

            print(f"{space}{myValue}", end="")

        print("")

    print("")
