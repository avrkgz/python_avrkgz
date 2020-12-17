# set
# new_set = {1,2,3,4,5,1,1,2,3,4}
# print(new_set)
# new_list = [1,2,3,4,5,1,1,2,3,4]
# print(new_list)
# new_list = set(new_list)
# print(new_list)
# new_set1 = {2,4,1,3,8,5,9,7,6}
# print(new_set1)

# new_set = set()
# set_ = {}
# print(type(set_))
# print(type(new_set))
# print(len(new_set))


# method add
# method update

# a_set = {1, 2}
# a_set.add(4)
# print(a_set)
# a_set.add('4')
# print(a_set)
#
# b_set = {5,6,7,8}
# a_set.update(b_set)
# print(a_set)


# method remove
# a_set.remove(1)
# print(a_set)

# method discard
# a_set.discard(2)
# a_set.remove(1)
# print(a_set)

# method pop, method clear
# print(a_set.pop())
# a_set.clear()
# print(a_set)


# # # # # # # # # # # # # # method union # # # # # # # # # # # # # # # # # # # # # #
# a_set = {2, 4, 5, 9, 12, 21, 30, 51, 76, 127, 195}
# b_set = {1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127}
# a_set.union(b_set)
# print(a_set)

# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# set2 = {2, 4, 6, 8, 222, 333, 444}
# print(set2.union(set1))


# # # # # # # # # # # # # METHOD intersection # # # # # # # # # # # # # #
# set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# set_2 = {2, 4, 6, 8, 222, 333,444}
#
# set_3 =set_1.intersection(set_2)
# print(set_3)


# # # # # # # # # # # # # # METHOD difference # # # # # # # # # # # # # #
# print(set_1.union(set_2)) # Slojenie
# print(set_1.intersection(set_2)) # Peresechenie
# print(set_1.difference(set_2)) # Raznost
# print(set_1.symmetric_difference(set_2)) # Semitrichnaya raznost
# # # # # # # # # # # METHOD summetric_difference # # # # # # # # # # # #



# # # # # # # # # # # # # # METHOD boolean # # # # # # # # # # # # # #

# x = True
# y = False
#
# if x < 0:
#     print(type(True))
# elif y < 0:
#     print(True)
# else:
#     print('Сработал блок else')
# print('hello')

# == СРАВНЕНИЕ
# != ОТРИЦАНИЕ
# < МЕНЬЩЕ
# >БОЛЬЩЕ
# <=МЕНЬШЕ РАВНО
# >=БОЛЬШЕ РАВНО
# and и
# or или
# not не

# point = input('Enter your point')
# if point == "5":
#     print("Молодец")
# elif point == "4":
#     print("Хорошо")
# elif point =="3":
#     print("Удовлетворительно")
# else:
#     print("ДВА!!!")


# list_ = [1, 2, 3, 4, 5]
# num = int(input('Enter a number'))
# if num in list_:
#     print('Такое чтсло есть')
# else:
#     print('Такого числа нет')
#
#
# num = int(input('Enter a number'))
# if num not in list_:
#     print('Такого чтсла нет')
# else:
#     print('Есть такое число')








# number1 = int(input('Enter a number'))
# number2 = int(input('Enter a number'))
#
# if number1 > 5 and number2 > 10:
#     print(number1 - number2)
# elif number1 > 5 or number2 > 10:
#     print(number1 + number2)
# # Для калькулятора добавить функцию OPERATOR
# import math
# while True:
#     number1 = input('Enter a number 1')
#     number2 = input('Enter a number 2')
#     number3 = input('Enter a number 3')
#     operator = input('enter a operator +-/*: ')
#     if operator == '+':
#         print('Вы ввели 1')
#         print(number1 + number2 + number3)
#     elif operator == '-':
#         print(number1 - number2 - number3)
#     elif operator == '/':
#         print(number1 / number2)
#     elif operator == '*':
#         print(number1 * number2)
#     elif operator == 'stop':
#         print('Вы остановили цикл')
#         break
#     else:
#         print('Введите оператор + - / *')
