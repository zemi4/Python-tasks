'''Существует список, который содержит целые числа или другие вложенные списки.
Вы должны положить все целые значения, в один плоский список.'''


def flat_list(array):
    result = []
    for i in array:
        if type(i) == list:
            result.extend(flat_list(i))
        else:
            result.append(i)
    return result


if __name__ == '__main__':
    # assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
