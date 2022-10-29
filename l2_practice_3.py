# Ввести число, вывести все его делители

num = int(input("White your number: "))
dividers = [1, (num)]
for i in range(2, int(num ** 0.5) + 1):
    if num % i:
        continue
    else:
        dividers.append(i)
        dividers.append(int(num / i))

dividers = sorted(dividers)
dividers  = list(map(str, dividers))

print('Dividers: ' + ', '.join(dividers))
