
numbers = []
with open("L3_hw_fizzbuzznum", "r") as f:
    items = f.read().split("\n")
    for i in items[:-1]:
        numbers.append([int(n) for n in i.split(",")])
final_result = []
for nums in numbers:
    result = []
    for num in range(1, nums[2]+1):
        if num % nums[0] == 0 and num % nums[1] == 0:
            result.append("FB")
        elif num % nums[0] == 0:
            result.append("F")
        elif num % nums[1] == 0:
            result.append("B")
        else:
            result.append(str(num))
    final_result.append(' '.join(result))
print(final_result)

with open(r"L3_hw_fizzbuzznum_new.txt", "w") as file:
  for elem in final_result:
    file.write(elem + "\n")
    # file.close()

