nRunes, amtFriendship = map(int, input().split(' ')) 
runes = {} 

for _ in range(nRunes): 
    ri, vi = input().split() 
    runes[ri] = int(vi) 

_ = input()

selected = input().split(' ') 

framt = 0 

for rune in selected: 
    framt += runes[rune]

print(framt) 

if framt >= amtFriendship:
    print("You shall pass!")
else:
    print("My precioooous")