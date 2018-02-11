#checkio_Brackets
#coding:utf-8

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


#

##########
#1

def checkio(expression):
    level = 0 
    br = { '[': ']', '(':')', '{':'}'}  
    b = {0:''}
    for i in expression:
        if i == '[' or i == '(' or i == '{':
            level += 1
            b[level] = br[i]
        elif i == ']' or i == ')' or i =='}':
            if b[level] == i:
                b.pop(level)
                level -=1
            else:
                return False
        #if level < 0:
        #    return False
    if level == 0:
            return True
    else:
        return False

 #辞書に前半と後半をセットで格納し、チェックする。.popはindex指定で削除するメソッド。
 #途中の２行は要らない。levelが負になるのは削除しすぎた時。だがbの削除はかっこの種類と位置が一致した時のみ。
 #ゆえに消しすぎることは絶対にない。

##########
#2

def checkio(expression):
    import re
    
    # Remove numbers and operators from string
    brackets = re.sub('[0-9+-/*]','',expression)
    
    # As long as brackets is not empty, keep running loop
    while brackets:
        temp, brackets = brackets, brackets.replace("[]","").replace("()","").replace("{}","")
        
        # if temp == brackets is True, means that no pair of brackets was removed
        # Therefore whatever remains in the bracket variable is not a pair of brackets
        if temp == brackets:
            return False
    
    return True

 #頭いい。先に余計なものを全て削除しておいておけば、残った文字列の真ん中にかっこのセットができ続ける。ループ。


##########
#3

def checkio(expression):
    o, c, st = "{([", "})]",[False]
    for i in expression:
        if i in o:
           st.append(i)
        if st and i in c and o[c.index(i)] != st.pop():
            return False
    if len(st) != 1:
        return False   
    return True

 #list.popはindexを指定しない場合、最後尾の要素を削除する。
 #また、おそらく削除系メソッド共通なのだろうが、削除メソッド自体は削除した値を返す。
 #違った。list.pop()による削除は削除対象を返す。list.remove()はNoneを返す。

##########


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"