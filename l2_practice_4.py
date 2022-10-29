# Ввести число, вывести его разряды и их множители.

result='Discharges and multipliers: \n'
num = int(input("Write your digit: "))
temp =num

while temp > 1:
   discharges = temp%10
   result += str(discharges) + ': 1, '
   for i in range(2, int(discharges)):
       if discharges%i==0:
           result += str(i)+", "
   result+=str(discharges)+ '. \n'
   temp = temp//10

print(result)