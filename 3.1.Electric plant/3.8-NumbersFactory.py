#checkio_Brackets

##########
#MyAnswer

def checkio(number):
    
    ans=''
    for i in range(9,1,-1):
        while divmod(number,i)[1]==0:
            ans=str(i)+ans
            number//=i
    
    return int(ans) if number==1 else 0

#一桁の数を9から2まで大きい順に辿り、割り切れるなら一個付加、を繰り返して数を作る。

##########
#Error

checkio=lm=lambda x, t=9: int((str(lm(x//t,t))+str(t)) if not(divmod(x,t)[1]) else str(lm(x,t-1)) if t>2 else -1 if x!=1 else 0) if x>0 else 0

#完成せず。がんばって１行にしようとしたけど泥沼化したのでやめます　最後に出るあまりで例外処理するのが難しかった

##########
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"
    assert checkio(21) == 37, "2nd example"
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"

