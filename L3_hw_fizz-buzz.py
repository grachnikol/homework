numbers = []

with open("L3_hw_fizzbuzznum.txt", "r") as f:
    items = f.read().split("\n")
    for i in items[:-1]:
        numbers.append([int(n) for n in i.split(",")])

for nums in numbers:
    for num in range(1, nums[2]+1):
        if num % nums[0] == 0 and num % nums[1] == 0:
            print("FB", end = " ")
        elif num % nums[0] == 0:
            print("F", end = " ")
        elif num % nums[1] == 0:
            print("B", end = " ")
        else:
            print(num, end = " ")
    result = map(str, nums)
    print(result)


    with open(r"fizzbuzznum_new.txt", "w") as file:
     for line in result:
        file.write(result + '\n')
