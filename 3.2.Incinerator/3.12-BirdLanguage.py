#checkio BirdLanguage
#coding:utf-8

##########
#MyAnswer

import string
 
def translate(phrase):
    
    phl=list(phrase)
    VOW=set('aeiouy')
    CON=set(string.ascii_lowercase)-VOW
    
    for i in range(len(phl)):
        if phl[i] in CON:
            phl[i+1]='' 
        elif phl[i] in VOW:
            phl[i+1]=phl[i+2]='' 
    
    ans=''
    for i in phl:
        ans+=i

    return ans

#小難しいことなしで、愚直に処理していった。listにして、要素を空の文字列と置き換えることで、list長を一定にする。
#母音処理の時に子音後付加の母音をいじらないようにするのは、付加母音より必ず子音が先に来るので、特別な回避策はいらない。

##########
#Error

import string
import re

def translate(phrase):
    
    patCV=re.compile('[bcdfghjklmnpqrstvwxz][aeiouy]')    
    patV3=re.compile('[aeiouy]{3}')
    
    cnt=0
    itrCV=patCV.finditer(phrase)
    for m in itrCV:
        phrase=phrase.replace(phrase[m.start()-cnt:m.start()+2-cnt],phrase[m.start()-cnt],1)
        cnt+=1
        print(phrase)
    
    cnt=0
    itrV3=patV3.finditer(phrase)
    for m in itrV3:
        phrase=phrase.replace(phrase[m.start()-cnt:m.start()-cnt+3],phrase[m.start()-cnt],1)
        cnt+=2
        print(phrase)
    
    return phrase

#replaceが結局先頭のものしか削除できないため断念。


##########
#2


##########
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"


