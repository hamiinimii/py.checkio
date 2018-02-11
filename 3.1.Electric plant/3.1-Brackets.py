#checkio_Brackets

##########
#MyAnswer

import re

def checkio(expression):

    bgn = ['{', '(', '[']
    end = ['}', ')', ']']
    order = []

    for br in list(expression):
        if br in bgn:
            order.append(bgn.index(br))
        if br in end:
            order.reverse()
            if end.index(br) in order and order.index(end.index(br)) == 0:
                order.remove(end.index(br))
                order.reverse()
            else:
                return False
    
    return False if order else True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
