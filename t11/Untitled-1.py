def print_factors(number):
    print(number)
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
number = int(input())
print_factors(number)