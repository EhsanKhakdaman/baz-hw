def remove_a(string):
    new_string = string.replace('a', '')
    return new_string
input_string = input()
print(remove_a(input_string))