def find_prime_factors(n):
    temp = []
    for i in range(1, n):
        if n % i == 0:
            temp.append(i)
    return temp


def prime_check(num):
    if num < 2:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True


factors = find_prime_factors(600851475143)

for factor in factors:
    if prime_check(factor):
        print(factor)


# for i in range(10):
#     print(i)
