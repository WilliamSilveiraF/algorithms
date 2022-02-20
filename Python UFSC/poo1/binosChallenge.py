turns = int(input())
nums = list(map(int, input().split()))

multiple2 = 0
multiple3 = 0
multiple4 = 0
multiple5 = 0


for num in nums:
    if num % 2 == 0:
        multiple2 += 1
    if num % 3 == 0:
        multiple3 += 1
    if num % 4 == 0:
        multiple4 += 1
    if num % 5 == 0:
        multiple5 += 1

print(f"{multiple2} Multiplo(s) de 2\n"
      f"{multiple3} Multiplo(s) de 3\n"
      f"{multiple4} Multiplo(s) de 4\n"
      f"{multiple5} Multiplo(s) de 5")