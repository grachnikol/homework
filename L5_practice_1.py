#Написать 2 функции. Первая функция будет принимать строку и приводить ее к нижнему регистру.
#Вторая функция будет принимать строку и проводить ее к верхнему регистру.
#После чего с помощью map применить ваши функции к списку строк. Отдельно каждую функцию к отдельному списку строк!


my_str = ['My string 1', 'My string 2', 'My string 3']

def lower_str(string):
    return string.lower()
def upper_str(string):
    return string.upper()

print(list(map(lower_str, my_str)), (list(map(upper_str, my_str))))
