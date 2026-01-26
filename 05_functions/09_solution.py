def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


for even_number in even_generator(15):
    print(even_number)
