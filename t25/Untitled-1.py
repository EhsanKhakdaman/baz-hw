def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
input_array = []
for num in input_array:
    print(f"The factorial of {num} is {factorial(num)}")
