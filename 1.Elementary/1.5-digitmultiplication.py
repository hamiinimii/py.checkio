#checkio_DigitsMultiplication
#coding:utf-8

##########
#MyAnswer

from functools import reduce
from operator import mul

def checkio(number):
    
    num=list(map(int,str(number)))
    ans=1
    
    for i in num:
        if i!=0:
            ans=ans*i
    
    return ans


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


##########
#1

def checkio(number):
    """
    Convert into the string and iterate.
    """
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res

    #行数はこうして少なくできる。if elseの内包表記は良い。

##########
#2

from functools import reduce
from operator import mul

def checkio(number):
    return reduce(mul, (int(x) for x in str(number) if x != '0'))

    #reduceは含まれるもの同士の計算をする。演算子の関数表記（掛け算mulなど）はimportが必要。
