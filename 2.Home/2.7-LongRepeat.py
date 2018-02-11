#checkio_PawnBrotherfood

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

#簡単な構造だが、正しい答えを出すのに必要なifの構造を間違えた。チェックしてからrunすべし。

