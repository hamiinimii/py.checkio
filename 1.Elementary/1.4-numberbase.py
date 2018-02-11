#checkio_NumberBase

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


