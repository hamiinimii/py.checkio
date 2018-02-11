#checkio_HousePassword
#coding:utf-8

##########
#MyAnswer

import re
def checkio(data):

    return False if (len(data)<10 or\
    #re.findall(r'[a-z]',data)==[] or\
    #re.findall(r'[A-Z]',data)==[] or\
    #re.findall(r'[0-9]',data)==[])\
    re.search(r'[a-z]',data)==None or\
    re.search(r'[A-Z]',data)==None or\
    re.search(r'[0-9]',data)==None)\
    else True

    #正規表現による検索。
    #searchは一致する表現があった場合に位置(matchオブジェクト)を返し、なかったらNoneを返す。
    #findallはマッチする部分文字列を全て探し出しリストとして返す。なかったら空のリスト

##########
#1


##########
#2

##########
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
