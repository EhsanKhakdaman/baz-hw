n = int(input())
fibonacci_numbers = [0, 1]
while fibonacci_numbers[-1] < 100000:
    new_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(new_number)
for number in fibonacci_numbers:
    if number % n == 0:
        print(number)