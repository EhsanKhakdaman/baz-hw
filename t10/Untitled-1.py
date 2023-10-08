number = int(input())
number_str = str(number)
new_number_str = ""
for digit in number_str:
    if digit != '0':
        new_number_str += digit
new_number = int(new_number_str)
print(new_number)