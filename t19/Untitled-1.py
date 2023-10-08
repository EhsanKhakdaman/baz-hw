def print_numbers(string):
    for char in string:
        if char.isdigit():
            print(char)
input_string = input()
print()
print_numbers(input_string)