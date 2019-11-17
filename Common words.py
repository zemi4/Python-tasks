'''Ваша функция должна находить все слова, которые появляются в обеих строках.
 Результат должен быть представлен, как строка со словами разделенными запятыми и отсортированными в алфавитном порядке.'''


def checkio(first, second):
    common = [i for i in first.split(",") if i in second.split(",")]
    common_s = sorted(common)
    return ','.join(common_s)


# решение lambda
# checkio = lambda first, second: ','.join(sorted(set(first.split(',')).intersection(second.split(','))))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
