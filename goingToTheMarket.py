trips = int(input())

for _ in range(trips):
    dictionary = {}
    count = 0
    products = int(input())
    for _ in range(products):
        product = input().split()
        nameProduct = product[0]
        priceProduct = float(product[1])
        dictionary[nameProduct] = priceProduct

    amt = int(input())

    for _ in range(amt):
        amount = input().split()
        nameProduct = amount[0]
        amtProduct = float(amount[1])
        count += dictionary[nameProduct] * amtProduct

    print(f"R$ {count:.2f}")