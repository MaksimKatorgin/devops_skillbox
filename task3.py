N = int(input('Введите число: '))
while N<=0:
    print('Число должно быть положительным')
    N = int(input('Введите число: '))
sum_number=0
count=0

while N>0:
    sum_number+=N%10
    count+=1
    N//=10

print('\nСумма цифр: ',sum_number,'\nКол-во цифр в числе: ',count)
print('Разность суммы и кол-ва цифр: ',sum_number-count)