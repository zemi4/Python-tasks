'''Ваша задача - посчитать суммарное количество шагов которое потребуется,
чтобы подобрать все 3 предмета - ('C' - compass), ('M' - map), ('S' - spyglass), считая от вашей стартовой позиции.
Таким образом, итоговый результат будет суммой трех дистанций: от Y к C, от Y к M и от Y к S (не Y-C-M-S).'''


def navigation(seaside):
    y = [0, 0]
    c = [0, 0]
    m = [0, 0]
    s = [0, 0]

    for i in range(len(seaside)):
        for j in range(len(seaside[i])):
            if seaside[i][j] == 'Y':
                y = [i, j]
            elif seaside[i][j] == 'C':
                c = [i, j]
            elif seaside[i][j] == 'M':
                m = [i, j]
            elif seaside[i][j] == 'S':
                s = [i, j]

    total = 0
    for item in [c, m, s]:
        x_distance = abs(y[0] - item[0])
        y_distance = abs(y[1] - item[1])
        total += max([x_distance, y_distance])

    return total


if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      ['M', 0, 0, 0, 'S']]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[0, 0, 'C'],
                       [0, 'S', 0],
                       ['M', 'Y', 0]]) == 4

    assert navigation([[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 'M', 0, 'S', 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 'C', 0, 0, 0],
                       [0, 'Y', 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
