def print_factorials(n):
    for i in range(n):
        number = int(input())
        factorial = calculate_factorial(number)
        print( number , factorial)
def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial
n = int(input())
print_factorials(n)