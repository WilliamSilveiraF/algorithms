bills = [100, 50, 20, 10, 5, 2]

while True:
    value, payment = map(int, input().split())

    diff = value - payment

    #for note in bills:
        