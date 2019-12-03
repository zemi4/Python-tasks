'''В качестве входных данных вы получите многострочную строку, состоящую из '0' и '#' - вид стены сверху.
'#' будут показывать каменную часть стены, а '0' - пустоты. Относительное расположение вас и стены следующее: вы смотрите на массив с нижней его части.
Ваша задача - найти координаты места, где стена наиболее узкая'''


def stone_wall(wall):
    wall = wall.split()
    weak_spots = [0] * len(wall[0])
    for item in wall:
        for i, part in enumerate(item):
            if part == '0':
                weak_spots[i] += 1
    return weak_spots.index(max(weak_spots))


# def stone_wall(wall):
#     wall = wall.split()
#     rows = ["".join(i) for i in zip(*wall)]
#     wall_thickens = [item.count("0") for item in rows]
#     return wall_thickens.index(max(wall_thickens))


if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    assert stone_wall('''
##########
####0##0##
00##0###00
00########
''') == 0

    assert stone_wall('''
##0
###
###
''') == 2

    print("Coding complete? Click 'Check' to earn cool rewards!")
