def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, int) and res > 1:
            is_not_prime = False
            for j in range(2, res):
                if res % j == 0:
                    is_not_prime = True
            if is_not_prime:
                print('Составное')
            else:
                print('Простое')
        return res
    return wrapper

@is_prime
def sum_three(num1, num2, num3):
    if isinstance(num1, int) and isinstance(num2, int) and isinstance(num3, int):
        return num1 + num2 + num3
    else:
        return None

result1 = sum_three(1, 1, 9)
print(result1)
print()
result2 = sum_three(1, 1, 10)
print(result2)


