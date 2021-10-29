def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    # Using dict comprehensions:
    # my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(my_dict)

    import math

    reto = {i: math.sqrt(i) for i in range(1, 1001) }
    print(reto)


if __name__ == '__main__':
    run()
