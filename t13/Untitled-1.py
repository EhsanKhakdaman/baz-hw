def print_numbers_with_difference_from_average():
    numbers = []
    for i in range(5):
        number = int(input())
        numbers.append(number)
    average = sum(numbers) / len(numbers)
    for number in numbers:
        if abs(number - average) > 3:
            print(number)

print_numbers_with_difference_from_average()