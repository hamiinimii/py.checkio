#checkio_HousePassword

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

