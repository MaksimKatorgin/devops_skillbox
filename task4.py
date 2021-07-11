def turn(num):
    def part(num):
        return ''.join(reversed(num))

    num_split = str(num).split('.')
    count = len(num_split[1])
    num1 = num_split[0]
    num2 = num_split[1]

    return(int(part(num1))+int(part(num2))/10**count)

N = turn(float(input('Введите первое число: ')))
K = turn(float(input('Введите второе число: ')))

print('\nПервое число наоборот:',N)
print('Второе число наоборот:',K)
print('\nСумма:',N+K)