# down below are the answer that i wrote previously
def second_highest(students):
    students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
    students_new = []
    for s in students:
        name = s[0]
        score = s[1]
        students_new.append([s[1], s[0]])
    students_new.sort(reverse = True)
    print(students_new[1][1])
    print(students_new[2][1])

second_highest('Tom')