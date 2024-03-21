4#Вывести на экран таблицу из 4 строк:
# три товара и сумма c циклом
summ = 0
tbl = ''
tovar = input('Чего желаете?')
from random import randint
while tovar != 'все':
    price = randint(50, 100)  #int(input('Сколько стоит? '))
    count = int(input(str(price) + ' рублей за штуку. Сколько штук?'))
    tbl += tovar + ' ' + str(price) + ' ' + str(count) + ' ' + str(price*count) + '\n'
    summ += price * count
    tovar = input('Чего-то ещё?')
print('Товар цена количество сумма')
print(tbl)
print('С вас ', summ, ' рублей')