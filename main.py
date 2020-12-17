# new_list =[]
# empity_list = list()
# list_ = [1,2,3,4,5,6]
# print(list_)
# print(len(list_))
#
# diapazon = range(1,21)
# print(list(diapazon))
# #
# # # method append   DOBAVLAYET ELEMENTY V KONCE SPISKA
# # some_list = [1,2,3,4,5]
# # print(some_list)
# # some_list.append(6)
# # print(some_list)
# # some_list.append('Python')
# # print(some_list)
# # print(len(some_list))
# # new_list = [1,2,3]
# # some_list.append(new_list)
# # print(some_list)
# # print(len(some_list))
#
# # method extend RASHIRYAET SPISOK, DRUGIM SPISKOM
#
# list1 = ('user1','user2','user3')
# list2 = ('anvar', 'rezvan', 'roma')
# list3 = list1 + list2
# list1 += list2
# list.extend(list2)
#
# print(list1)
# print(list1)
#
# # method insert POLUCHAET 2 ARGUMENTA I DOBAVLAET V SPISOK POINDEKSNO
#
# cars = ['Audi', 'Honda', 'Mercedes']
# print(cars)
# cars.insert(0, 'Toyota')
# print(cars)

# method remove UDALYAET ELEMENT PO ZNACHENIU

# laptops = ['Lenovo', 'MacBook', 'Acer', 'Asus', 'Hp']
# laptops.remove('Asus')
# print(laptops)
# laptops.remove('MacBook')
# print(laptops)\

# method pop UDALYAET POSLEDNIY ELEMENT PO UMOLCHANIU, NO MOJNO PEREDAT INDEX UDALENNOGO ELEMENTA

# laptops = ['Lenovo', 'MacBook', 'Acer', 'Asus', 'Hp']
# notebook = laptops.pop(1)
# last_notebook = laptops.pop()
# print(laptops)
# print(notebook)
# print(last_notebook)

# method index VOZVROSHAET INDEX ELEMENTA

# laptops = ['Lenovo', 'MacBook', 'Acer', 'Asus', 'Hp']
# print(laptops.index('Lenovo'))

# method count

# numbers = [1,2,3,4,1,2,3,1,1,1,2,2]
# print(numbers.count(1))

# method reverse RAZVORACHIVAET SPISOK

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers.reverse()
# print(numbers)

# method sort SORTIRUET PO KLUCHU

# nums = [1,2,3,4,5,6,7]
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)
# laptops = ['Lenovo', 'MacBook', 'Acer', 'Asus', 'Hp']
# laptops.sort(key=len, reverse=True)
# print(laptops)

# method copy

# cars = ['Audi', 'Honda', 'Mercedes', ['Hello', 'World']]
# print(cars)
# new_cars = cars.copy()
# new_cars[3][0] = 'BMW'
# print(new_cars)
#
# numbers = [1,2,3,4,5,[6,7,8,9]]
# numbers_2 = numbers.copy()
# numbers_2[5][0] = "shest"
# print(numbers)


# method deepcopy

# import copy
# list_ = [1,2,3,[4,5,6]]
# print('Original', list_)
# new_list =copy.deepcopy(list_)
# print('Copy', new_list)
# new_list[3][0] = 'Changed'
# print('copy', new_list)
# print('Original', list_)

# method clear POLNOSTYU UDALYAET
# method del UDALYAET PO INDEKSU

# cars = ['Audi', 'Honda', 'Mercedes']
# cars.clear()
# del cars[1]
# print(cars)


# srezy

# list_ =[1,2,3,4,5,6,7,8,9]
# print(list_[0:5])
# print(list_[::2])


# KORTEJI - tuples

# new_tuple = ('abc',)
# print(type(new_tuple))
# tuple_=tuple()
# print(type(tuple_))
# print(dir(tuple_))


