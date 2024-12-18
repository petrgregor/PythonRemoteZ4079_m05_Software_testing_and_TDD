def word_count(s):
    return len(str(s).split())


if __name__ == "__main__":
    words = ["Hello      world",
             "This is a test",
             "One more test case",
             "",
             "Python is awesome!"]
    for word in words:
        print(f"'{word}' has length {word_count(word)}")
