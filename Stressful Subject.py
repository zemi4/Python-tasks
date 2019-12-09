'''Функция должна распознавать является ли тема письма стрессовой. Стрессовая тема определяется тем, что все буквы
в верхнем регистре, и / или заканчиваются как минимум тремя восклицательными знаками, и / или содержат по крайней мере
одно из следующих слов-маркеров: "help", "asap", "urgent". Любое из этих слов-маркеров может быть написано по-разному:
 «HELP», «help», «HeLp», «H! E! L! P!», «H-E-L-P», и даже очень непринужденно «HHHEEEEEEEEELLP».'''

from itertools import groupby


def is_stressful(subj):
    if subj.isupper():
        return True
    subj = subj.lower()
    result = []
    for letter in subj:
        if letter == 'h' or letter == ' ' or letter == 'e' or letter == 'l' or letter == 'p' or letter == 'a' or letter == 's' or letter == 'u' or letter == 'r' or letter == 'g' or letter == 'n' or letter == 't' in subj:
            result.append(letter)

    letter = [key for key, group in groupby(result)]

    a = ''.join(letter)

    if 'help' in a or 'asap' in a or 'urgent' in a or '!!!' in subj[-3:]:
        return True
    return False

    # return True if (re.search(r'[hH]+\W*[eE]+\W*[lL]+\W*[pP]+|[aA]+\W*[sS]+\W*[aA]+\W*[pP]+|[uU]+\W*[rR]+\W*[gG]+\W*[eE]+\W*[nN]+\W*[tT]+|!{3,}$', subj)) or subj.isupper() else False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    assert is_stressful("h!e!l!p") == True
    assert is_stressful("UUUURGGGEEEEENT here") == True
    assert is_stressful("something is gona happen") == False
    assert is_stressful("Heeeeeey!!! I’m having so much fun!”") == False
    assert is_stressful("Hello puppy") == False
    print('Done! Go Check it!')
