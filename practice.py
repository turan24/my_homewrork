# Задача 1. Курьер
#
# Вам известен номер квартиры, этажность дома и количество квартир на этаже. Задача: написать функцию, которая по
# заданным параметрам напишет вам, в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.

numbers_apartment_at_floor = 4
floors = 8
apartment = 36

all_flat_in_entrance = numbers_apartment_at_floor * floors

if apartment % all_flat_in_entrance:
    entrance = apartment // all_flat_in_entrance + 1
else:
    entrance = apartment // all_flat_in_entrance

number_apartment_in_entrance = all_flat_in_entrance * entrance - apartment

x = floors - number_apartment_in_entrance // numbers_apartment_at_floor

print(f'Номер квартиры - {apartment}, подъезд - {entrance}, этаж - {x}')

#
# Задача 2. Бриллиант
#
# Входным данным является целое число. Необходимо:
#
# написать проверку, чтобы в работу пускать только положительные нечетные числа
# для правильного числа нужно построить бриллиант из звездочек или любых других символов и вывести его в консоли.
# Для числа 1 он выглядит как одна взездочка, для числа три он выглядит как звезда,
# потом три звезды, потом опять одна, для пятерки - звезда, три, пять, три, одна...

count = 1
while True:
    user_number = int(input('Enter the odd number: '))
    if user_number % 2:
        break
    elif count > 2:
        print('Это такое число, которое делится с остатком на 2!')
    else:
        print('Enter нечетное число!!!!')
        count += 1


star = 1
reverse = False

for i in range(1, user_number + 1):
    space = int((user_number - star) / 2)
    print(f"{' ' * space}{'*' * star}")
    if not reverse:
        star += 2
    else:
        star -= 2
    if star == user_number:
        reverse = True




# Задача 3. Файл-тест. Есть файл, в котором хранятся числа в следующем формате:
#
# Цифры до точки с запятой надо суммировать, потом делить на их количество.
# В первой строке сумма будет 11, разделить на их количество, т.е. на 3, получается 3 целых и в остатке 2.
# Аналогичным образом во второй строке 6 делим на три, ровно два и в остатке ноль, в третьей строке сумма 16, на 5 делим,
# получаем 3 и 1 в остатке. Вот так:
#
# Задача: проверить каждую строку файла, если строка записана верно, вывести ее и после написать True,
# если строка не верна, вывести результат с пометкой False.



with open('practice3.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        line_1 = line.split(';')[0]
        line_2 = line.split(';')[1]
        current_sum = 0
        count = 0
        for c in line_1:
            if c.isdigit():
                current_sum += int(c)
                count += 1
        check_number = []
        for c in line_2:
            if c.isdigit():
                check_number.append(int(c))

        check = True if current_sum // count == check_number[0] and current_sum % count == check_number[1] else False
        print(f'{line} - {check}')