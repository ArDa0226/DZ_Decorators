

def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        k = 0
        for i in range(2, res - 1):
            if res % i == 0:
                k += 1
            if k <= 0:
                return f'Простое число {res}'
            else:
                return f'Составное число {res}'
    return wrapper

@is_prime
def sum_three(*args):
    total = 0
    for n in args:
        total += n
    return total

result = sum_three(2, 3, 6)
print(result)


# res_2 = is_prime(sum_three(result))
# print(res_2)