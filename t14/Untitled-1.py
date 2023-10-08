def print_prime_numbers(n):
    prime_count = 0
    for i in range(n):
        number = int(input())
        if is_prime(number):
            prime_count += 1
    print( prime_count)
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
n = int(input())
print_prime_numbers(n)
