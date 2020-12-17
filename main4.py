# from datetime import datetime
#
# start = datetime.now()
# some_list = [i for i in range(200000)]
# # print(some_list)
# finish = datetime.now()



# start2 = datetime.now()
# some_list2 = []
# for i in range(200000):
#     some_list2.append(i)
# # print(some_list2)
# finish2 = datetime.now()

## ----------------------------------------------##

# even = [num for num in range(50) if num % 2 == 0 and num % 6 == 0]
# print(even)


# my_func = lambda x,y: x+y
# print(my_func(10, 10))
#
# def add(x,y):
#     return x + y
# print(add(10, 10))


# #----------------------------------------------##


# list_ = [1,2,3,4,5,6,7,8,9]
# def my_func(x):
#     return x ** x
#
# new_list = list(map(my_func, list_))
# print(new_list)



# nums = [1,2,3,4,5]
# def my_func(x):
#     x += 10
#     return x
#
# nums2 = list(map(my_func, nums))
# print(nums2)



# text = 'I love Python'
#
# def my_func(x):
#     return x.upper()
#
# text2 = list(map(my_func, text))
# print(text2)
# text3 = ''.join(text2)
# print(text3)



# #----------------------------------------------##



# mixed = ['mak', 'mak', 'proso', 'mak', 'proso', 'mak']
# my_filter = lambda x: x == 'mak'
# zolushka = list(filter(my_filter, mixed))
# print(zolushka)

# from functools import reduce
#
# nums = [x for x in range(50)]
# lambda_func = lambda x, y: x + y
# summ_all = reduce(lambda_func, nums)
# print(summ_all)



# #----------------------------------------------##



# text = 'hello world'
# nums = [x for x in range(20)]
# tuple_ = ('a', 'b', 'c', 'd', 'e')


# zip_fune = list(zip(text, nums, tuple_))
# print(zip_fune)

# tuple_ = tuple(zip(text, nums))
# print(tuple_)

# dict_ = dict(zip(text, nums))
# print(dict_)



# #----------------------------------------------##



 