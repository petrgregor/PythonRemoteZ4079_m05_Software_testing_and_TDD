def odd_indexes(string):
    return str(string)[1::2]


if __name__ == "__main__":
    words = ["elephant", "computer", "Petr", 123456789]
    for word in words:
        print(f"{word} -> {odd_indexes(word)}")