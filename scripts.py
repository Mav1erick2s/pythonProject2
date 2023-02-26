per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму:"))
deposit=list(per_cent.values())

def per_cent1(mon):
    return mon*money
deposit=(list(map(per_cent1, deposit)))

max_deposit= max(deposit)
print(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max_deposit)

