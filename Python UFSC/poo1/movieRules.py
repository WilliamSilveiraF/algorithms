ageA = int(input())
ageB = int(input())

if ageA < 6 or ageB < 6:
    print("NO")
elif ageA >= 18 or ageB >= 18:
    print("YES")
elif ageA >= 14 and ageB >= 14:
    print("YES")
else:
    print("NO")