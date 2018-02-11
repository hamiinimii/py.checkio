#checkio_NumberBase
#coding:utf-8

##########
#MyAnswer

def checkio(str_number, radix):
    

    li_st2=[chr(s) for s in range(ord('A'),ord('Z')+1)]
    li_st3=[(str(i),i) for i in range(36)]
    for j in range(10,36):
        li_st3[j]=(li_st2[j-10],j)

    cnvtr=dict(li_st3)
    
    ans=0
    
    for i in range(len(str_number)):
        if cnvtr[str_number[-i-1]]>=radix:
            ans=-1
            break
        else:
            ans=ans+(radix**i)*cnvtr[str_number[-i-1]]
    
    return ans

##########
#1

def checkio(str_number, radix):
    try: 
        return int(str_number, radix)
    except:
        return -1

    #intがもとより頭良すぎ問題。そのまま文字列、基数の順で打ち込むと10進数にしてくれる。
    #ただし、不適切な場合 -1 を返せとの問題。try/exceptの例外処理で-1を返させる。


##########


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A = 10"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")