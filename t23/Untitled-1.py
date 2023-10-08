def is_sorted_descending(array):
    sorted_array = sorted(array, reverse=True)
    return array == sorted_array
input_array = input().split()
input_array = [int(x) for x in input_array]
if is_sorted_descending(input_array):
    print("The numbers are sorted in descending order.")
else:
    print("The numbers are not sorted in descending order.")