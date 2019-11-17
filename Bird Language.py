'''после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
- после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa)'''

VOWELS = "aeiouy"


def translate(phrase):
    i = 0
    result = []
    while i < len(phrase):
        result.append(phrase[i])
        if phrase[i] in VOWELS:
            i = i + 3
        elif phrase[i] == ' ':
            i += 1
        else:
            i = i + 2

    return ''.join(result)


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
