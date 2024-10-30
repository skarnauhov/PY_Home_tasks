def summmm(a):
    pass

def minnnn():
    pass

def apply_all_func(int_fl_list, *functions):
    results = {}
    for func in functions:
        func_res = 'Ошибка!'
        try:
            func_res = func(int_fl_list)
        except:
            print(f'В списке {int_fl_list} должны быть только числа. А функции должны работать со списками чисел.')
        finally:
            try:
                results[func.__name__] = func_res
            except:
                print(f'Похоже "{func}" не является функцией, результат её работы не записан в словарь.')
    return results

print(apply_all_func([6.6, 20, 15, 9], max, min))
print(apply_all_func([6.6, 20, 15, 9], len, sum, sorted))
print()
print(apply_all_func(['6.6', 20, 15, 9], max, min))
print(apply_all_func([6.6, 20, 15, 9], max, minnnn))
print(apply_all_func([6.6, 20, 15, 9], len, '1234', summmm, sorted, 1))

