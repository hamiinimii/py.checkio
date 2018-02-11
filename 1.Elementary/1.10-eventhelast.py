#checkio_EvenTheLast

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

