def func(number):
    return int(str(number)[::2]) * 2


if __name__ == "__main__":
    inputs = [12, 11, 2, 4, 123, 92, 79, 19023]
    for input_ in inputs:
        print(f"{input_} -> {func(input_)}")
