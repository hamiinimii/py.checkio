#checkio_ThreeWords
#coding:utf-8

##########
#MyAnswer

def checkio(words):
    
    cnt=0
    wl=list(words)
    #「' 'の前後に文字がある」を連続して2回。
    while (cnt<2 and ' ' in wl):
        if (wl[wl.index(' ')-1].isdigit()==False\
        and wl[wl.index(' ')+1].isdigit()==False):
            cnt+=1
            print(cnt)
        else:
            cnt=0
        wl.remove(' ')
            
    return True if cnt==2 else False
    
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

##########
#Fail

def checkio(words):
    
    cnt=0
    spc=0
    
    for i in range(len(words)):
        if words[i].isdigit()==False:
            if spc==1:
                cnt+=1
            elif words[i]==' ':
                spc=1 
        else:
            cnt=0
            
        if cnt==2:
            break
    
    return True if cnt==2 else False



##########
#1

import re
def checkio(words):
    return bool(re.compile("([a-zA-Z]+ ){2}[a-zA-Z]+").search(words))

 #正規表現
 #アルファベット1文字以上の繰り返しが2回、そしてアルファベット1文字以上の繰り返しを1回
 #前2回には' 'が入れてあり、その2つの後に' 'がない1個を繋げることで3語連続に一致する
  #' 'は'\s'にしたほうがわかりやすかろう
 #さて、コンパイルした正規表現を表すオブジェクトに、メソッドを使う（コンパイル前でもできる）
 #searchは文字列内で一致する場所を返すメソッド（複数あっても1回のみ）
 #boolは真偽判定のbool値を返す。1以上なら真を返し、0やNoneなら偽を返す


##########
#2

def checkio(words):
    succ = 0
    for word in words.split():
        succ = (succ + 1)*word.isalpha()
        if succ == 3: return True
    else: return False

    #wordsの文字列をsplitで分割。
    #isalphaで英字のみなら1、違えば0が入るのでそれで連続判定
    #3連続した時点でTrueを返す、以降超えたり0になったりしても問題ない。
    #一度も3にならなければforが終わり、forが終わってしまうと終了処理elseでFalseを返す

##########
#3

import re

def checkio(words):
    return bool(re.search('\D+ \D+ \D+', words))

    #正規表現\D（非数字）などで対象をこう表せる
    #search(pattern,string)でpatternをstringから探す
    #すると#1が変に見える。コンパイルした文字列に.search()は、コンパイル文字列で()を調べられるのか。

##########
#4

import re
def checkio(words):

    return True if 'True, True, True' \
    in ''.join(str([x.isalpha() for x in words.split()])) else False

    #for内包表記はリストの中でしかできないのかな。strの中でやってみようとしたらエラー吐いた。
    #ていうかこのjoinいらんわ。join引数の時点でもともと'[True, True, ...]'な文字列吐いてるわ。
    #だから、

   #in str([x.isalpha() for x in words.split()]) else False

    #でOK。なおjoinはリスト要素を連結した文字列を出力する目的で使う。


##########


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
