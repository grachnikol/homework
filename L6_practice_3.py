# Написать функцию перевода размеров женского белья из международного во все
# остальные. Внтри функции нужно просто обращаться к правильно составленному
# словарю.
dresses_pants = {'S': "Russia_40, Sweden_34, France_36,Italy_38, UK_8, USA_6",
                 'M': "Russia_42, Sweden_36, France_38, Italy_40, UK_10, USA_8",
                 'ML': "Russia_44, Sweden_38, France_40, Italy_42, UK_12, USA_10",
                 'L': "Russia_46, Sweden_40, France_42, Italy_44, UK_14, USA_12",
                 'XL': "Russia_48, Sweden_42, France_44, Italy_46, UK_16, USA_14"
                 ,}


def sizes(size):
    return dresses_pants.keys

my_size=input()
print(sizes(my_size))



