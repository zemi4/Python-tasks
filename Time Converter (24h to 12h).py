def time_converter(time):
    hour, minute = time.split(':')
    am_pm = "p.m."

    if 12 > int(hour):
        am_pm = "a.m."
        if int(hour) == 0:
            hour = 12

    elif 12 < int(hour):
        hour = int(hour) - 12
    return "{}:{} {}".format(int(hour), minute, am_pm)


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
