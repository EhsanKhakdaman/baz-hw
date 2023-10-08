def print_sorted(array):
    sorted_array = sorted(array, reverse=True)
    for number in sorted_array:
        print(number)
input_array = input().split()
input_array = [int(x) for x in input_array]
print_sorted(input_array)