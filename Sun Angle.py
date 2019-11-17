''' определить угол солнца над горизонтом, зная время суток. Исходные данные: солнце встает на востоке в 6:00, что соответствует углу 0 градусов.
В 12:00 солнце в зените, а значит угол = 90 градусов. В 18:00 солнце садится за горизонт и угол равен 180 градусов.
В случае, если указано ночное время (раньше 6:00 или позже 18:00), функция должна вернуть фразу "I don't see the sun!".'''


def sun_angle(time):
    a = int(time[0:2]) * 60 + int(time[3:5])
    return "I don't see the sun!" if a > 1080 or a < 360 else (a - 360) * 0.25


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("12:15") == 93.75
    assert sun_angle("01:23") == "I don't see the sun!"
