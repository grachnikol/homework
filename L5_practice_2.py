# Написать функцию которая будет простое число возводить в квардрат.
# Необходимо возвести в квадрат все простые числа в списке используя функцию map

def square_number(x):
    return x**2

num_list=[]
num=int(input('Write your number: '))
for i in range(1, num+1):
    if not i%2:
        continue
    else:
        num_list.append(i)

print(list(map(square_number, num_list)))