''' если результаты забегов выглядят следующим образом [[“1:13”, “1:26”, “1:11”], [“1:10”, “1:18”, “1:14”], [“1:20”, “1:23”, “1:15”]]
 Тогда самой быстрой лошадью будет №3, так как она победила в 2 забегах из 3.'''


def fastest_horse(horses: list) -> int:
    # replace this for solution
    return 0


if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
