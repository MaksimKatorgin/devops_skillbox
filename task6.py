x = float(input('Введите координату X: '))
y = float(input('Введите координату Y: '))
r = float(input('Введите радиус R: '))
while r < 0:
    print('Радиус не м.б. отрицательным')
    r = float(input('Введите радиус R: '))

hyp = (x**2+y**2)**0.5

if hyp <= r:
    print('\nМонетка где-то рядом')
else:
    print('\nМонетки в области нет')