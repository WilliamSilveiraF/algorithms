num, ratio = map(int, input('Digite um número: ').split(' '))
for num in range(num, num + ratio * 10, ratio):
    print(num)