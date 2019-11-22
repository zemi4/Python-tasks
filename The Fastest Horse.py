''' если результаты забегов выглядят следующим образом [[“1:13”, “1:26”, “1:11”], [“1:10”, “1:18”, “1:14”], [“1:20”, “1:23”, “1:15”]]
 Тогда самой быстрой лошадью будет №3, так как она победила в 2 забегах из 3.'''

from itertools import groupby


def fastest_horse(horses: list) -> int:
    winners = [i.index(min(i)) + 1 for i in horses]
    winning_counts = [(k, len(list(g))) for k, g in groupby(sorted(winners))]
    winner = sorted(winning_counts, key=lambda x: x[1])[-1][0]
    return winner


if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    assert fastest_horse([["4:44", "4:11", "4:18"], ["3:10", "3:01", "3:14"], ["2:20", "2:23", "2:15"]]) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
