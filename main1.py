# Dictionary - slova
# new_dict = {}
# new_dict2 = dict()
# print(new_dict)
# print(new_dict2)
# print(type(new_dict))
# print(type(new_dict2))
# print(dir(new_dict))
#
# new_dict ={'key': 'value'}


# capitals = dict()
# capitals['Kyrgyzstan'] = 'Bishkek'
# capitals['Russia'] = 'Moscow'
# print(capitals)
#


# capitals = dict(Russia='Moscow', Kyrgystan='Bishkek', USA='Washington' )
# print(capitals)
#
# capitals = dict([('Russia','Moscow'), ('Kyrgystan','Bishkek'), ('USA','Washington')])
# print(capitals)

# new_dict = dict(zip(['Russia', 'Kyrgyzstan', 'USA'],['Moscow', 'Bishkek', 'Washington']))
# print(new_dict)

# method fromkeys SOZDAET SLOVAR IZ KLUCHEY
# dictionary = dict.fromkeys(['key1','key2'])
# print(dictionary)
#
# method get POLUCHAET ZNACHENIE PO KLUCHU
# capitals = dict(Russia='Moscow', Kyrgyzstan='Bishkek')
# print(capitals.get('Russia'))
#
# numbers = {'1':'2',3:4:5:6 }
# print(number['1'])
# numbers[7] = 8
# print(numbers)
# numbers[3] = 11111
# print(numbers)

# method keys VYVODIT VSE KLYUCHI IZ SLOVARYA
# method valuev VYVODIT VSE ZNACHENIYA
# method items VOZVROWAET PARU KLUCH I ZNACHENIE
# method pop UDALYAET PO KLUCHU I VOZVRAWAET ZNACHENIE

# capitals =dict(Russia='Moscow', Kyrgyzstan='Bishkek' )
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# russia = capitals.pop('Russia')
# print(russia)
# print(capitals)

# method update

# capitals = dict(Russia='Moscow', Kyrgyzstan='Bishkek', USA='Washington')
# capitals2 = {'Belarus': 'Minsk', 'Russia': 'Vladivostok'}
# capitals.update(capitals2)
# print(capitals)

# method popitem NE PRINIMAET ARGUMENT, UDALYAET POSLEDNIY ELEMENT
# capitals = dict(Russia='Moscow', Kyrgyzstan='Bishkek', USA='Washington')
# capitals.popitem()
# print(capitals)


# method setdefault
# capitals = dict(Russia='Moscow', Kyrgyzstan='Bishkek', USA='Washington')
# new = capitals.setdefault('Kyrgyzstan')
# print(new)
# print(capitals)