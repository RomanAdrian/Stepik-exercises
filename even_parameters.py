def even_numbers(*args):

    only_numbers = [i for i in args if isinstance(i, (int))]
    rez_numbers = []

    for i in only_numbers:
        if (i % 2 == 0):
            rez_numbers.append(i)
    return rez_numbers
print(even_numbers("maria", 3, "alex", 20, 24, 6))
