'''Пароль считается достаточно стойким, если его длина больше или равна 10 символам, он содержит,
 как минимум одну цифру, одну букву в верхнем и одну в нижнем регистре. Пароль может содержать только латинские буквы и/или цифры.'''


def checkio(data: str) -> bool:
    if any(x.isupper() for x in data) == True:  # верхний регистр
        if any(x.isdigit() for x in data) == True:  # из цифр
            if any(x.islower() for x in data) == True:  # нижний регистр
                if len(data) >= 10:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('erer798rew9rew9r7ew987rw') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
