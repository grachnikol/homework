# Создать словарь оценок предполагаемых студентов
# (Ключ - ФИ студента, значение - список оценок студентов).
# Найти самого успешного и самого отстающего по среднему баллу.

students_dict = {"Ivasenko Luda": [11, 2, 6, 8],
            "Prekrasnaja Nastya": [4, 12, 8, 7],
            "Naumova Vika": [9, 8, 10, 12],
            }

def average_list(lst):
    return sum(lst) // len(lst)

points = sorted(students_dict.keys(), key = lambda studentid: average_list(students_dict[studentid]))

print("The best: ", points[-1] )
print("The worst: ", points[0])



