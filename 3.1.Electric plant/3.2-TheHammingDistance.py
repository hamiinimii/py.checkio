#checkio_Brackets
#coding:utf-8

##########
#MyAnswer

from numpy import zeros
def checkio(n, m):
    
    ans=0
    
    nl=list(str(bin(n)))
    nl.reverse()
    nl.remove('b')

    ml=list(str(bin(m)))
    ml.reverse()
    ml.remove('b')
    
    min(nl,ml,key=len).extend(list(zeros(abs(len(nl)-len(ml)),int)))
    
    for (i,j) in zip(nl,ml):
        ans+=abs(int(i)-int(j))
        
    return ans

 #数の長さ調整はzerosの追加で行なっている。
 #min(nl,... のところは、+=で書こうとすると'SyntaxError: can't assign to function call'
 #代わりにメソッドの.extendを使ったらOK.

##########
#1

FORMAT = '{0:0>32b}'

def checkio(n, m):
    n = FORMAT.format(n)
    m = FORMAT.format(m)
    return sum([1 for i, _ in enumerate(n) if n[i] != m[i]])

 #format関数。よく使われる形式は次の通り。
 #'任意の文字列{}任意の文字列'.format(変数)

##########
#2



##########

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
