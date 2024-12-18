from functools import reduce


def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError
    if n < 1:
        raise ValueError
    if n == 1:
        return 0
    a, b = 0, 1
    for _ in range(1, n-1):
        a, b = b, a + b
    return b


def fibonacci_reduce(n):
    if not isinstance(n, int):
        raise TypeError
    if n < 1:
        raise ValueError
    return reduce(lambda acc, _: (acc[1], acc[0] + acc[1]), range(1, n), (0, 1))[0]


if __name__ == "__main__":
    for i in range(1, 21):
        print(f"fib({i}) = {fibonacci(i)}")
    #print(fibonacci(-5))
    #print(fibonacci("5"))
    #print(fibonacci(3.8))
