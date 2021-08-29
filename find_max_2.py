# down below are the answer that i wrote previously
# def second_highest(students):
#     students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
#     students_new = []
#     for s in students:
#         name = s[0]
#         score = s[1]
#         students_new.append([s[1], s[0]])
#     students_new.sort(reverse = True)
#     print(students_new[1][1])
#     print(students_new[2][1])
# second_highest('Tom')

# teachers answers are down below
def second_highest(students):
    grades = [s[1] for s in students] # 只把成績拿出來
    # 以下是16行的擴寫(18~20行)
    # grades = []
    # for s in students:
    #     grades = s[1]
    grades = sorted(grades, reverse=True)
    second = grades[1] # grades[0]是最高，grades[1]是第二高
    
    # 再下來找誰是這個分數
    # 底下這句話的意思是拿到 所有分數跟第二高一樣的人的"人名"也就是s[0]的部分
    # 記得嗎 參數的這個students清單裡面的東西，s[0]是人名，s[1]是分數
    second_high_students = [s[0] for s in students if s[1] == second]
    # 以下是27行的擴寫
    # for s in students:
    # if s[1] == second:
    #     second_high_students.append(s[0])
    for student in second_high_students:
        print(student)
