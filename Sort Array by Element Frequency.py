'''Сортируйте заданную итерацию так, чтобы ее элементы оказались в порядке убывания частоты, то есть,
 сколько раз они появляются в элементах. Если два элемента имеют одинаковую частоту,
  они должны заканчиваться в том же порядке, что и первое появление в итерируемом.'''
from itertools import groupby


def frequency_sort(items):
    result = []

    for i in items:
        result.append(i)

        for a in items:
            if a == result[-1] in items:
                result.append(a)
    print(result)
    return result


# [key for key, group in groupby(items)]

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
