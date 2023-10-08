num = input(())
num_str = str(num)
result = ""
for digit in num_str:
    if digit != '0':
        result += digit
print(result)