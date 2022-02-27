a, b = list(map(float, input().split(' ')))
if a == 1:
    price = 4.00
if a == 2:
    price = 4.50
if a == 3:
    price = 5.00
if a == 4:
    price = 2.00
if a == 5:
    price = 1.50

print('Total: R$ {:.2f}'.format(price * b))
