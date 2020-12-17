# Цикл for
import time
# x = 0
# for i in range(20):
#     x += 1
#     print('Pyrhon', x)

# numbers = []

# for number in range(20):
#     numbers.append(number)
#     # print(numbers)
#     time.sleep(0.3)
#
# print(numbers)


# Range (начало конец шаг)

# text = 'i love python'
# for i in text:
#     print(i.upper())
#     if i == ' ':
#         break

#                         Чётные числа
# for i in range(50):
#     if i % 2 == 0:
#         print(i)


# while i <= 10:
#     print('True')
#     i += i


# i = 0
# while True:
#     i += 1
#     print(i)
#     if i == 10:
#         break

# total = 100
# i = 0
# while i < 5:
#     n = int(input('input number'))
#     total -= n
#     i += 1
# print('Total', total)


# i = 0
# while i < 20:
#     print('Текстовая строка')
#     i = i + 1
#     if i == 10:
#         print('Continue')
#         continue
#     print('Continue не сработало')
#     if i == 18:
#         print('break')
#         break


# def is_palindrome():
#     text = input('Input World')
#     if text == text[::-1]:
#         print('its palindrom')
#     else:
#         print('not')
# is_palindrome()



# def hello():
#     print('Hello')
#                           нужно вызывать
# hello()



# name = input('Input your name: ')
# def hello(name):
#     print(f"Hello, {name}")
#                             нужно вызывать
# hello(name)


# def add(x, y):
#     return x + y
#
# print(add(10, 20))

# name = 'Anvar'
# def my_func():
#     print(name)
# my_func()
########################################\

# def my_func():
#     name = 'Anvar'
#     print('Print ' + name)
#
# my_func()
#
#
#
# def my_func(x, y):
#     z = x ** y
#     return z
#
# var = my_func(2,3)
# print(var)


# num = 2222
# def my_func():
#     num = 111
#     print(num)
# my_func()
# print(num)


# def add(q,w,e,r,t,y,u,i,o,p):
#     return q + w + e + r + t + y + u + i + o + p
# print(add(1,2,3,4,5,6,7,8,9,0))
#
# def add2(*args):
#     result = 0
#     for i in args:
#         for x in i:
#             result += x
#     return result
#
# nums = [1,2,3,4,1,2,3,4,1,2,3,4,5]
#
# print(add2(nums))


# def my_func(x,y,z=10):
#     return x+ y+z
# print(my_func(,1,2,-10))
# vars('Hello')
# print(var.var, sep='____')

# name = 'Anvar'
# def myfunc(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key} is {value}")
#
# myfunc(a=1,b=2,c=3)


import time
# def recursive_function():
#     print('У попа была собака, он ее любил')
#     print('Она сьела кусок мяса, он ее убил')
#     print("В землю закорал, надпись написвл")
#     time.sleep(0.2)
#     recursive_function()
#
# recursive_function()


