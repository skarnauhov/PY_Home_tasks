def print_param(a=1, b='string', c=True):
    print(a, b, c)

print_param()
print_param(b=25)
print_param(c=[1, 2, 3])
print_param(1, 2, 3)
print_param(2)

values_list = [56.4, False, [2, 1]]
values_list_2 = [False, [2, 1]]
values_dict = {'a': 31.2, 'b': True, 'c': 'hello'}

print_param(*values_list)
print_param(**values_dict)
print_param(*values_list_2, 42)