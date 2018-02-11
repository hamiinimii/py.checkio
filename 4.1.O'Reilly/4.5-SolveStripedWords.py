#checkio_SolveStripedWords


##########
#Answer

import re

V = "aeiouy"


def checkio(text):
    cnt = 0
    words = re.split('[.,!? ]', text)
    for w in [x for x in words if len(x)>1 and x.isalpha()]:
        v = 1 if w.lower()[0] in V else 0
        for i in w.lower()[1:]:
            if (i in V) != v:
                v=not v
            else:
                break
        else:
            cnt += 1
    return cnt

##########

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    assert non_repeat('') == '', "Null"
    print('"Run" is good. How is "Check"?')
