#checkio_EvenTheLast
#coding:utf-8

##########
#MyAnswer

def checkio(array):

    try:
        return array[-1]*sum(array[0::2])
    except:
        return 0

    #2ステップ刻みでarrayから要素を抽出。スタートは0番目からになるので偶数番目のものを取り出せる

##########
#Failure

def checkio(array):

    try:
        return array[-1]*sum([i for i in array if array.index(i)%2==0])
    except:
        return 0

    #arrayに同じ数字が2回入っていると、indexは常に1個目のインデックスを返すので、取りこぼす。

##########
#1

def checkio(array):

    try:
        return array[-1]*sum([x for (i, x) in enumerate(array) if i%2==0])
        
    except:
        return 0

    #enumerateはループにおいてインデックス付きで要素を得る関数（index, object）。
    #ループで便利なのは他にzip。複数のシーケンスオブジェクトを同時にループできる。


##########
#2

def checkio(array):
    """
    The simple slice and comprehension.
    """
    return sum(el for el in array[::2]) * array[-1] if array else 0

    #arrayが空の場合はじかなくてはならないが、それはarrayで真偽判定した時偽になることを意味する。


##########
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
