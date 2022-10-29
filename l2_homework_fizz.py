# fizz-buzz
#У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz.
# До третьего необходимо досчитать от единицы. Считая, надо выводить число.
# Если число кратно fizz - надо выводить F вместо числа.
# Если число кратно buzz - надо выводить B вместо числа.
# Если число кратно и fizz и buzz, надо выводить FB. И так - пока не будет достигнуто третье введенное число.

result = []
fizz, buzz, num = int(input("Fizz: ")), int(input("Buzz: ")), int(input("Num: "))
for i in range (1, num+1):
    if not i%fizz and not i%buzz :
        result.append( 'FB')
    elif not i%fizz:
        result.append( 'F')
    elif not i%buzz:
        result.append( 'B')
    else:
        result.append(str(i))
print('  '.join(result) )