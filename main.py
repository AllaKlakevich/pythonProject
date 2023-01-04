# n = -5
# if n > 0:
#     print('положительное')
# elif n < 0:
#     print('отрицательное')
# else:
#     print('равно нулю')

# a = int(input('Введите число'))
# print(a ** 2)

# a = int(input('Введите первое число'))
# b = int(input('Введите второе число'))
# if a * a == b or b * b == a:
#     print('Да')
# else:
#     print('Hет')
#
# max = int(input('введите число'))
# for i in range(4):
#     a = int(input('введите число'))
#     if a > max:
#         max = a
# print(max)
#
# lst = []
# for i in range(5):
#     a = int(input('введите число'))
#     lst.append(a)
# print(max(lst))
#
# n = int(input('введите число'))
# for i in range(-n,n + 1):
#     print(i,end=' ')

# a = float(input('введите число: '))
# print(int(a*10%10))

# a = input('Введите число: ').split(".")
# if len(a) > 1:
#     print(a[1][0])
# else:
#     print('0')

# n = int(input('введите число'))
# if n % 30 == 0:
#     print('Не соответстует')
# elif n % 5 == 0 and n % 10 ==0 or n % 15 == 0:
#     print('Соответстует')
# else:
#     print('Не делится')

n = int(input('введите число'))
if n % 30 == 0:
    print('Не соответстует')
elif n % 5 == 0 and n % 10 == 0 or n % 15 == 0:
    print('Соответстует')
else:
    print('Не делится')