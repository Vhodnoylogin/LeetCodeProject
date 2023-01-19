def square(x: float):
    return x * x


def run():
    my_number = input()
    try:
        my_number = float(my_number)
        print(square(my_number))
    except TypeError as e:
        print(e)