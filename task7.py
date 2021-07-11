def count(num):
    count_max = str(num).count(str(num % 10))
    first_num = str(num).count(str(num // 1000))
    if first_num > count_max:
        count_max = first_num

    return count_max

first_year = int(input('Введите первый год: '))
last_year = int(input('Введите второй год: '))
while len(str(first_year)) != 4 or len(str(last_year)) != 4:
    print('Числа д.б. четырёхзначными')
    first_year = int(input('Введите первый год: '))
    last_year = int(input('Введите второй год: '))

print('\nГода от', first_year, 'до', last_year, 'с тремя одинаковыми цифрами:')
while first_year <= last_year:
    if count(first_year) == 3:
        print(first_year)
    first_year += 1