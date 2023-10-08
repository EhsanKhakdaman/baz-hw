number =int(input())

number_str = str(number)

zero_count = 0
for digit in number_str:
    if digit == '0':
        zero_count += 1

print(zero_count)