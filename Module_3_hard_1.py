#sum_ = 0

def dict_summator(dict_, s = 0):
    sum_ = s
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
            sum_ = dict_summator(value, sum_)
        else:
            sum_ = calculate_structure_sum(value, sum_)
        #print(sum_)
    return sum_


def calculate_structure_sum(list_, s = 0):
    sum_ = s
    for i in list_:
        #print(i)
        if isinstance(i, (int, float)):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, dict):
            sum_ = dict_summator(i, sum_)
        else:
            #print(i)
            sum_ = calculate_structure_sum(i, sum_)
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

#sum_ = 0

result = calculate_structure_sum(data_structure_2)
print(result)