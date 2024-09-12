numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    if numbers[i] > 1:
        is_not_prime = False
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                is_not_prime = True
                break
        if is_not_prime:
            not_primes.append(numbers[i])
        else:
            primes.append(numbers[i])
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')