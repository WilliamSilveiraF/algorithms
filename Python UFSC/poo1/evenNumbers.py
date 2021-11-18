n = int(input())
x = 1
while x in range(1, n+1):
    if x % 2 != 0:
        print(x)
    x += 1