def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
input_array = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
output_array = []

for num in input_array:
    if not is_prime(num):
        output_array.append(num)
print(output_array)