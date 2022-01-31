while True:
    turns = int(input())
    if turns == 0: break
    results = input().split(' ')
    print(f"Mary won {results.count('0')} times and John won {results.count('1')} times")
