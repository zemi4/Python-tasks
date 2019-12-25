'''Все слова в строковом представлении числа должны быть разделены одним пробелом. Будьте осторожны с
пробелами -- очень сложно увидеть двойной пробел, но это критично для компьютера.'''

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    result = []
    hundred = number // 100
    number %= 100
    tens = number // 10
    ones = number % 10
    if hundred > 0:
        result.append(FIRST_TEN[hundred - 1])
        result.append(HUNDRED)
    if tens > 1:
        result.append(OTHER_TENS[tens - 2])
    if tens == 1:
        result.append(SECOND_TEN[ones])
    elif ones > 0:
        result.append(FIRST_TEN[ones - 1])

    return ' '.join(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    # assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(59) == 'fifty nine', "4th example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
