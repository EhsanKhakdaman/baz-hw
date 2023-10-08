def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

odd_count = 0
fibonacci_count = 0

for i in range(100):
    if i % 2 != 0:
        odd_count += 1
    if is_fibonacci(i):
        fibonacci_count += 1

print(odd_count)
print( fibonacci_count)