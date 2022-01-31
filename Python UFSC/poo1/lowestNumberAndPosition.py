amount = int(input())
myNums = input().split(' ')

smallest = myNums[0]
smallest = min(myNums)

print(f"Menor valor: {smallest}")
print(f"Posicao: {myNums.index(smallest)}")


