n = int(input("Please input number of students: "))

allStudents = []

for i in range(n):
    student = []
    name = str(input("Enter name : "))
    grade = int(input("Enter grade : "))
    student.append(name)
    student.append(grade)
    allStudents.append(student)





for i in range(len(allStudents)):
    for j in range(len(allStudents)-1):
        if allStudents[j][1] > allStudents[j+1][1]:
             temp = allStudents[j]
             allStudents[j] = allStudents[j + 1]
             allStudents[j + 1] = temp


print(allStudents)

least = allStudents[0][1]
print(least)
for i in range(len(allStudents)):
    score = allStudents[i][1]
    if score == least:
        allStudents.remove(allStudents[i])


secondleast = allStudents[0][1]

secondleaststudents = []

for i in range(len(allStudents)):
    if allStudents[i][1] == secondLeast:
        secondleaststudents = secondleaststudents.appened(allStudents[i])

if len(secondleaststudents) > 1:

    def getKey(item):
        return item[0]

    sorted(secondleaststudents, key=getKey)

for i in range(len(secondleaststudents)):
    print(secondleaststudents[i][0])
    print(secondleaststudents[i][1])


