'''Положительные целые числа могут быть выражены в виде сумм последовательных положительных целых чисел различными
способами. Например, 42 можно выразить как такую сумму четырьмя различными способами: (а) 3+4+5+6+7+8+9, (б) 9+10+11+12,
 (в) 13+14+15 и (г) 42. Как показывает последнее решение (г), любое положительное целое число всегда можно тривиально
 выразить в виде одноэлементной суммы, состоящей только из этого целого числа.'''


def count_consecutive_summers(num):
    result = 0

    for i in range(1, num + 1):
        addition = 0
        for number in range(i, num + 1):
            addition += number
            if addition == num:
                result += 1
            elif addition > num:
                break

    return result


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
