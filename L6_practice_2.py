# Создать структуру данных для студентов из имен и фамилий, можно случайных.
# Придумать структуру данных, чтобы указывать, в какой группе учится студент (Группы Python, FrontEnd,
# FullStack, Java). Студент может учиться в нескольких группах. Затем вывести:
# студентов, которые учатся в двух и более группах
# студентов, которые не учатся на фронтенде
# студентов, которые изучают Python или Java

Python = {1: "Ivasenko Luda", 2: "Prekrasnaja Nastya"}
FrontEnd = {1: "Naumova Vika"}
FullStack = {1: "Ivasenko Luda", 2:"Naumova Vika"}
Java = {1: "Radchuk Sveta", 2: "Oliynik Iryna"}

pyth_java=[]
non_front=[]
for i in Python, FrontEnd, FullStack, Java:
        if i == Python or i == Java:
            pyth_java.append(i.values())
        if i != FrontEnd:
            non_front.append(i.values())


print("Python and Java students: ", pyth_java)
print("Not FrontEnd students: ", non_front)








