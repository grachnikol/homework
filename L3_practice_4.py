# Банкомат выдает сумму максимально возможными купюрами

cash = int(input("Write your summ: "))

denomination = [500, 200, 100, 50, 20, 10, 5, 2, 1]
banknotes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(denomination)):
   while cash>=denomination[i]:
        cash-=denomination[i]
        banknotes[i]+=1
        if cash<denomination[i]:
            print (denomination[i], '-', banknotes[i], 'banknotes')