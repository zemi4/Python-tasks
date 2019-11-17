''' Есть ли в исходной строке три слова подряд.'''


def checkio(words: str) -> bool:
    n = 0
    for i in words.split():
        if i.isalpha():
            n += 1
        else:
            n = 0
            continue
        if n == 3:
            return True

    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
