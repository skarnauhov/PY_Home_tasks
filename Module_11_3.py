import sys
from pprint import pprint
from Module_6_hard import Circle


def intorspection_info(obj):
    i_info = {}
    i_attributes = []
    i_methods = []
    i_methods_wr = []
    i_methods_b_in = []
    i_module = ''
    i_builtin = False
    python_ver = ''
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if str(type(attr)) == "<class 'method'>":
            i_methods.append(attr_name)
        if str(type(attr)) == "<class 'method-wrapper'>":
            i_methods_wr.append(attr_name)
        if str(type(attr)) == "<class 'builtin_function_or_method'>":
            i_methods_b_in.append(attr_name)
        if attr_name == '__dict__':
            for key, value in attr.items():
                i_attributes.append(key)
        if attr_name == '__module__':
            i_module = attr
        # print(attr_name, attr, type(attr))
    i_info['1. type'] = type(obj)
    type_name = str(i_info['1. type']).split(' ')
    if type_name[1][1:-2:] in dir(__builtins__):
        i_builtin = True
    i_info['2. built_in'] = i_builtin
    i_info['3. attributes'] = i_attributes
    i_info['4. module'] = i_module
    i_info['5. methods'] = i_methods
    i_info['6. methods_wrapper'] = i_methods_wr
    i_info['7. methods_built_in'] = i_methods_b_in
    python_ver = str(sys.version).split(' ')[0]
    if python_ver == '3.12.4':
        return i_info
    else:
        return print('Ваша версия питона не поддерживается, для работы программы необходима версия 3.12.4\n'
                     'или измените условие в строке 40 на своё усмотрение :)')

class SomeClass:
    pass

a = SomeClass()
b = 453
c = 'sdf'
circle1 = Circle((200, 200, 100), 10)

print(f'Текущая версия питона: {str(sys.version).split(' ')[0]}')
print(intorspection_info(a))
print(intorspection_info(b))
print(intorspection_info(c))
pprint(intorspection_info(circle1))