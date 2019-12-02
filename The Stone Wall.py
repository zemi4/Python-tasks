'''В качестве входных данных вы получите многострочную строку, состоящую из '0' и '#' - вид стены сверху.
'#' будут показывать каменную часть стены, а '0' - пустоты. Относительное расположение вас и стены следующее: вы смотрите на массив с нижней его части.
Ваша задача - найти координаты места, где стена наиболее узкая'''


def stone_wall(wall):
    if '0' not in wall:
        return 0
    x = wall.split()
    result = []
    for i in x:
        for a in enumerate(i):
            if a[1] == '0':
                result.append(a[0])

    for b in sorted(result):
        if result.count(b) > 1:
            return b


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

#     assert stone_wall('''
# ##0
# ###
# ###
# ''') == 2

    print("Coding complete? Click 'Check' to earn cool rewards!")
