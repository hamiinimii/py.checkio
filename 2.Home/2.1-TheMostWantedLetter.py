#checkio_TheMostWantedLetter
#coding:utf-8

##########
#MyAnswer

import re
def checkio(text):

    tlist=list(re.sub(r'[^a-zA-Z]','',text.lower()))
    return sorted(sorted(tlist,reverse=True),key=tlist.count)[-1]    

    #1.2を応用。正規表現で英字以外を消した後、sortedを使って並べ替え。
    #sortedでアルファベット逆順に並べた後、countで数えて小さい順に整列。
    #一度目の整列をある程度保持するらしく、順番が入れ替わることなく答えにたどり着ける。

##########
#1
def checkio(text):

    dict = {text.lower().count(char): char for char in sorted(set(text.lower()), reverse=True) if char.isalpha()}
    return dict[max(dict)]

    #数を数える時に便利な辞書dictionaryくん。keyを文字、値を個数とすれば良い。
    #と思いきや、keyを個数、値を文字としている。つまり、同じ個数の文字を一つしか格納しないようにしている。
    #char(acter)に、元文字列の中から集合として取り出した諸々を格納しそれを逆順に整頓。
    #これにより最終結果として、同じ個数の文字の内、アルファベット順で早いものが残ることを考えよう。
    #sortedでcharという集合(set)の中身は逆アルファベット順に整頓されている。
    #つまり辞書への格納の処理の順番はcharの前から処理していることになる。
    #概ねfor inなどで取り出しながら処理をしていく場合、前から順に処理される（当たり前だけど、とても大切なこと）


##########
#2
import string
def checkio(text):

    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)

    #string.ascii_lowercaseはstringのモジュールに定義されている定数。小文字列'abc...xyz'を返す。
    #（stringの定数には色々な文字列があるので応用するといい）
    #text中の個数でこのアルファベット列から判定。
    #maxでは、同数のものが見つかった時は最も先に来たものを返すらしい。
    #前から処理するのは共通で、順に辿っただけで終わらせた時かその全体を俯瞰した時かで違うように見えるだけか

##########
#3

from collections import Counter

def checkio(text):
    count = Counter([x for x in text.lower() if x.isalpha()])
    m = max(count.values())
    return sorted([x for (x, y) in count.items() if y == m])[0]

    #collectionsモジュールを使う。Counterはdictのサブクラス、ハッシュ可能なオブジェクトをカウントする。
    #Counterは存在しない要素に対してKeyErrorではなく0を返す。

##########
#4

def checkio(text):
    s = list(text.lower())
    letters = [s.count(chr(x)) for x in range(97,123)]
    
    return chr(97+letters.index(max(letters)))

##########


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

