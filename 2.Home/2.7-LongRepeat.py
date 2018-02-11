#checkio_PawnBrotherfood
#coding:utf-8

##########
#MyAnswer

def long_repeat(line):
    
    temp=['',0,0]
    for i in list(line):
        if i == temp[0]:
            temp[1]+=1
        else:
            temp[0]=i
            temp[1]=1
        if temp[1]>temp[2]:
            temp[2]=temp[1]
    
    return temp[2]

#簡単な構造だが、正しい答えを出すのに必要なifの構造を間違えた。チェックしてからrunしろ。

##########
#1

long_repeat = lambda l: bool(l) and max(sum(1 for _ in c) for _, \
c in __import__("itertools").groupby(l))

#1行python。
#groupbyがよくわからない。

##########

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
