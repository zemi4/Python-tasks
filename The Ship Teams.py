'''необходимо поделить всех нанятых матросов на 2 команды, согласно следующим правилам:
 те, чей возраст меньше 20 лет или больше 40 - отправляются на первый корабль, все остальные - на второй.'''


def two_teams(sailors):
    f = [i for i, j in sailors.items() if j < 20 or j > 40]
    s = [i for i, j in sailors.items() if j >= 20 and j <= 40]
    return [sorted(f), sorted(s)]


if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34,
        'Wesson': 22,
        'Coleman': 45,
        'Abrahams': 19}) == [
               ['Abrahams', 'Coleman'],
               ['Smith', 'Wesson']
           ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
               ['Fernandes', 'Kale', 'McCortney'],
               ['Johnson']
           ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
