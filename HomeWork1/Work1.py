# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#
# a = int(input('Введите число от 1 до 7'))
# if a == 6 or a == 7:
#     print('выходной')
# else:
#     print('будний день недели')
#

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#
# x = int(input('введите число по оси х '))
# y = int(input('введите число по оси у '))
# if x > 0 and y > 0:
#     print('первая четверть')
# elif x < 0 and y > 0:
#     print('вторая четверть')
# elif x < 0 and y < 0:
#     print('третяя четверть')
# elif x > 0 and y < 0:
#     print('четвертая четверть')
# else:
#     print('число не должно быть равно 0')

# # Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
#
# a = int(input('Введите номер четверти '))
# if a == 1:
#     print('x - положительное, у - положительное')
# elif a == 2:
#     print('x - отрицательное, у - положительное')
# elif a == 3:
#     print('x - отрицательное, у - отрицательное')
# else:
#     print('x - положительное, у - отрицательное')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве
x1 = float(input('введите координату х первой точки '))
y1 = float(input('введите координату y первой точки '))
x2 = float(input('введите координату х второй точки '))
y2 = float(input('введите координату y второй точки '))
dist = ((x2-x1)**2+(y2-y1)**2)**0.5
print('расстояние между точками ')
print(dist)