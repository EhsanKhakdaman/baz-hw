def find_max(array):
    max_number = max(array)
    return max_number
input_array = input().split()
input_array = [int(x) for x in input_array]
print(find_max(input_array))