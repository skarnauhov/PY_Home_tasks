#module_1_6.py
children = {'Anna': 2011, 'Sergey': 2010, 'Alla': 2015}
print("Dict:", children)
print("Existing value:", children['Alla'])
print("Not existing value:", children.get('Fedya'))
children['dog'] = 2021
children.update({'cat': 2023})
print("Deleted value:", children.pop('Anna')) # del children['Anna']
                            # print(children.get('Anna', 2011))
print("Modified dict:", children)

my_set = {'Anna', 'Alla', 'Anna', 2011, 2015, 2011, True, False, True}
print("SET:", my_set)
my_set.add(56.34)
my_set.add(6.3)
my_set.remove(2011)
print("Modified SET", my_set)

