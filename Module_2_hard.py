n = (int(input('Введите число от 3 до 20: ')))
code_elements_1 = []
code_elements_2 = []
result = []

for element in range(1, n):
    code_elements_1.append(element)
    code_elements_2.append(element)

for element_1 in code_elements_1:
    for element_2 in code_elements_2:
        if element_1 != element_2:
            if n % (element_1 + element_2) == 0 and element_1 < element_2:
                result.append(element_1)
                result.append(element_2)

print('Сим сим откройся: ', *result)