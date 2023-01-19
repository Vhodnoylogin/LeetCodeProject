from typing import List


def square_list(inp: List[int]):
    return [x * x for x in inp]


def run():
    my_numbers = input()
    try:
        my_numbers = my_numbers.split(',')
        my_numbers = [int(x) for x in my_numbers]
        print(square_list(my_numbers))
    except TypeError as e:
        print(e)