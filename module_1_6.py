my_dict = {'Gosha' : 2000, 'Julia' : 1989}
print('Dict:', my_dict)
print('Existing value:', my_dict['Gosha'])
print('Not existing value:', my_dict.get('Lena'))
my_dict.update({'Oleg' : 1990, 'Ivan' : 1972})
a = my_dict.pop('Julia')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
my_set = {23, 43, 55, 23, 55, True, False, True, 'Feder', 'Anna', 'Hans', 'Anna', (1, 1, 1, 2)}
print('Set:', my_set)
my_set.update({10, (0, 0, 7)})
my_set.remove(55)
print('Modified set:', my_set)