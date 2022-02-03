while True:
    try:
        turns = int(input())
        result = ''
        for _ in range(turns):
            binary = input()
            decimal = int(binary, 2)
            result += chr(decimal)
        print(result)
    except EOFError:
        break
