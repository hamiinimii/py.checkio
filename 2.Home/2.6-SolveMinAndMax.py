#checkio_PawnBrotherfood

##########
#MyAnswer

def min(*args, **kwargs):
    key = kwargs.get("key", None)
    
    # (len(args)==1)==(args is list)
    if len(args) == 1:
        arlst = list(args[0])
    else:
        arlst = list(args)

    arlst.reverse()

    Karlst=[]
    if key:
        for i in arlst:
            Karlst.append(key(i))
    else:
        Karlst=arlst

    temp = Karlst[0]
    for i in range(len(arlst)):
        if Karlst[i] <= temp:
            temp = Karlst[i]
            ans=arlst[i]

    return ans


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    
    # (len(args)==1)==(args is list)
    if len(args) == 1:
        arlst = list(args[0])
    else:
        arlst = list(args)

    arlst.reverse()

    Karlst=[]
    if key:
        for i in arlst:
            Karlst.append(key(i))
    else:
        Karlst=arlst

    temp = Karlst[0]
    for i in range(len(arlst)):
        if Karlst[i] >= temp:
            temp = Karlst[i]
            ans=arlst[i]

    return ans

	#要素をつなげて微修正を繰り返してできた一品。理解が不足していたところが多い。

