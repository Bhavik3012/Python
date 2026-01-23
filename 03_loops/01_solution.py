numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = []

for num in numbers:
    if num > 0:
        positive_number_count.append(num)

print("Positive numbers in the list:")
for positive_num in positive_number_count:
    print(positive_num)
