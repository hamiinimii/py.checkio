#checkio_LongNonRepeat
#coding:utf-8

##########
non_repeat=lm=lambda l:l if len(l)==len(set(l)) else max(lm(l[:-1]),lm(l[1:]),key=len)

#１行達成！
#最初はl*(bool式)にしていたが、その場合lの方が空だと無限ループに入る。のでif elseで分岐させた。


##########
#1

non_repeat=lambda s,r=range(99):max([s[i:j]for i in r for j in r],key=lambda x:len(x)*bool(len(x)==len(set(x))))

#forで二種類独立に回す時ってこうやって書けるんですね。
#引数でありうる長さの最大値を99とし、引数の文字列sから開始終了地点を回して部分抽出。
#長さ最大かつ重複無しを、key関数でlenにboolをかけることで達成。
#題意的に必要な一変数の指定に対し、もう一つ使う要素を第二変数のデフォルト値の形で導入。

##########

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    assert non_repeat('') == '', "Null"
    print('"Run" is good. How is "Check"?')
