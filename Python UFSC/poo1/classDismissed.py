studentsAmt, minStudentsForStartClass = map(int, input().split())

classes = list(map(int, input().split()))

punctualStudents = 0

for student in classes:
    if student <= 0:
        punctualStudents += 1
if punctualStudents >= minStudentsForStartClass:
    print("YES")
else:
    print("NO")
