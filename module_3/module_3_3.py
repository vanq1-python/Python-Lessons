def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['Hello', 2.3, [123, 2]]

values_dict = {'a' : False, 'b' : 3.14, 'c' : 'STOP'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['New', 32.1]

print_params(*values_list_2, 42)
