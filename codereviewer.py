import random
def get_coffee_partner(students):
    students_list = list(students)
    while True:
        random.shuffle(students_list)
        flag = False

        for student1, student2 in zip(students, students_list):
            if student1 == student2:
                flag = True
                break
        if not flag:
            return dict(zip(students, students_list))
