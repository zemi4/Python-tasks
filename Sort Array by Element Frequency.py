'''Сортируйте заданную итерацию так, чтобы ее элементы оказались в порядке убывания частоты, то есть,
 сколько раз они появляются в элементах. Если два элемента имеют одинаковую частоту,
  они должны заканчиваться в том же порядке, что и первое появление в итерируемом.'''


def frequency_sort(items):
    result = sorted(items, key=lambda x: items.index(x))
    result = sorted(result, key=items.count, reverse=1)
    return result


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
