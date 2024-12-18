def is_prime(n):
    if not isinstance(n, int):
       raise TypeError
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def factorial(n):
    if n < 0:
        raise ValueError
    result = 1
    for i in range(2, n+1):
        result *= i
    return result


if __name__ == "__main__":
    for i in range(21):
        print(f"Number {i}: is_prime({i}) = {is_prime(i)},\t\t"
              f"{i}! = {factorial(i)}")
