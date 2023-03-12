number_of_tickets = int(input('Введите колличество билетов: '))
coust = 0
for t in range(1, number_of_tickets+1):
    print("Введите возраст владельца билета:", t)
    age = int(input())
    if age < 18:
        coust += 0
    elif age < 25:
        coust += 900
    elif age >= 25:
        coust += 1390
print('Цена без скидки: ', coust, 'рублей')
if number_of_tickets > 3:
     discount = coust * 0.1
     coust -= discount
     print('Цена со скидкой: ', coust, 'рублей')