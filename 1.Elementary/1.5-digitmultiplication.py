#checkio_DigitsMultiplication

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

