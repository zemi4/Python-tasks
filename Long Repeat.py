'''Вам необходимо найти длину самой длинной подстроки, которая состоит из одинаковых букв.'''

from itertools import groupby


def long_repeat(line: str) -> int:
    if not line:
        return 0
    else:
        return max([len(list(group)) for key, group in groupby(line)])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
