turns = int(input())

while True:
    try:
        result = ''
        for turn in range(turns):
            binary = input()
            decimal = int(binary, 2)
            result += chr(decimal)
        print(result)
    except EOFError:
        break
