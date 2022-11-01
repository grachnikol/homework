# Банкомат выдает сумм мелкими, но не больше 10 штук каждой мелкой купюры
cash = int(input("Write your summ: "))

max_summa=1000*10
denomination = [1, 2, 5, 10, 20, 50, 100, 200, 500]
banknotes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range (len(denomination)+1):
    max_summa+=i*10

if cash>max_summa:
    print('Not enough available banknotes')

else:
    if not cash%10:
        banknotes[0]=10
        cash-=10
    else:
        banknotes[0]=cash%10
        cash-=banknotes[0]

    for i in range((len(denomination))+1):
        denomination.append(1000)

        if not i:
            continue
       if cash-(denomination[i]*10)>0 and not cash-denomination[i]*10%denomination[i+1]:
                    cash-=denomination[i]*10
                    banknotes[i]+=10
                else:
                    while cash<0 or cash%denomination[i+1]:
                        cash+=denomination[1]
                        banknotes[i]-=1
                        if not banknotes[i]:
                            break
    print (banknotes)




    # banknotes[0] = cash % 10
    # cash -= banknotes[0]
    # for i in range(len(denomination[:-1])):
    #     while cash >= denomination[i + 1] and banknotes[i + 1] < 10:
    #         cash -= denomination[i + 1]
    #         banknotes[i + 1] += 1
    # print(banknotes)
    # if cash > 0:
    #     print('Not enough available banknotes')


