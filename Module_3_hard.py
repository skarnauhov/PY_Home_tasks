sum_ = 0

def dict_summator(dict_):
    global sum_
    for key, value in dict_.items():
        #print(key, value)
        if isinstance(key, (int, float)):
            sum_ += key
        elif isinstance(key, str):
            sum_ += len(key)
        if isinstance(value, (int, float)):
            sum_ += value
        elif isinstance(value, str):
            sum_ += len(value)
        elif isinstance(value, dict):
            dict_summator(value)
        else:
            calculate_structure_sum(*value)
        #print(sum_)
    return


def calculate_structure_sum(list_):
    global sum_
    for i in list_:
        #print(i)
        if isinstance(i, (int, float)):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, dict):
            dict_summator(i)
        else:
            #print(i)
            calculate_structure_sum(i)
        #print('сумма:', sum_)
    return sum_


data_structure_1 = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

data_structure_2 = [
5,
5.1,
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': {'dict_in_dict': 3}}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure_1)
print(result)

sum_ = 0

result = calculate_structure_sum(data_structure_2)
print(result)