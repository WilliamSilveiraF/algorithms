n, m = map(int, input().split(' '))

p1 = n
p2 = m

def eh_Primo(num):
    for x in range(num, 0, -1):
        if num % x == 0 and x != 1 and x != num:
            return False
        elif x == 1:
            return True

while p1 > 0:
    if eh_Primo(p1):
        break
    p1 -= 1
while p2 > 0:
    if eh_Primo(p2):
        break
    p2 -= 1
print(p1 * p2)
