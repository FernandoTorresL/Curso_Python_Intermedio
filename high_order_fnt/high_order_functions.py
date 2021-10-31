def using_filter():

    # Get only odd numbers from a list
    print("USING FILTER")
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    print("Get only odd numbers from list", my_list)

    # Using list_comprehensions:
    odd = [i for i in my_list if i % 2 != 0]

    # Using high order function: filter
    odd2 = list(filter(lambda x: x%2 != 0, my_list))

    # Print result: [1, 5, 9, 13, 19, 21]
    print("Using list_comprehensions:", odd)
    print("Using high order function, filter:", odd2)

def using_map():

    # Get square numbers from a list
    print("USING MAP")
    my_list = [1, 2, 3, 4, 5]
    print("Get square numbers from list", my_list)

    # Using list_comprehensions:
    odd = [i**2 for i in my_list]

    # Using high order function: map
    odd2 = list(map(lambda x: x**2, my_list))

    # Print result: [1, 4, 9, 25]
    print("Using list_comprehensions:", odd)
    print("Using high order function, map:", odd2)

def using_reduce():

    # Get all the numbers from a list multiplied
    print("USING REDUCE")
    my_list = [2, 2, 2, 2, 2]
    print("Multiplied all the numbers from a list", my_list)

    # Using for:
    all_multiplied = 1
    for i in my_list:
        all_multiplied = all_multiplied * i

    # Using high order function: map
    from functools import reduce
    all_multiplied2 = reduce(lambda a, b: a * b, my_list)

    # Print result: 36
    print("Using for:", all_multiplied)
    print("Using high order function, reduce:", all_multiplied2)


if __name__ == '__main__':
    using_filter()
    print()

    using_map()
    print()

    using_reduce()
