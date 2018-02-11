#checkio_LongNonRepeat

##########
non_repeat=lm=lambda l:l if len(l)==len(set(l)) else max(lm(l[:-1]),lm(l[1:]),key=len)

#１行達成！
#最初はl*(bool式)にしていたが、その場合lの方が空だと無限ループに入る。のでif elseで分岐させた。


##########

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    assert non_repeat('') == '', "Null"
    print('"Run" is good. How is "Check"?')
