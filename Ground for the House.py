def house(plan):
    if '#' not in plan:
        return 0
    grid = plan.split()
    no_so = []
    east = []
    west = []
    for index, line in enumerate(grid):
        if '#' in line:
            no_so.append(index)
            east.append(line.find('#'))
            west.append(line.rfind('#'))
    return (max(no_so) - min(no_so) + 1) * (max(west) - min(east) + 1)


if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
