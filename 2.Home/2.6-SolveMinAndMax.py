#checkio_PawnBrotherfood
#coding:utf-8

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

##########
#1

def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]

def min(*args, key=None):
    return get_first_from_sorted(args, key, False)

def max(*args, key=None):
    return get_first_from_sorted(args, key, True)


#は？？？？みじか
#えずるくない？？というかスマートだけども可変長引数のチャレンジ皆無だから教育上は良くないね
#sortedにreverseの有無を添えてやることでmaxとminが達成されるのだ



  
##########
#2

def min(*a, **kw):
    k = kw.get("key", lambda x: x)
    m=None
    g=a[0] if len(a)==1 else a
    for i in g:
        if m==None:
            m=i
        m=i if k(i)<k(m) else m
    return m

def max(*a, **kw):
    k = kw.get("key", lambda x: x)
    m=None
    g=a[0] if len(a)==1 else a
    for i in g:
        if m==None:
            m=i
        m=i if k(i)>k(m) else m
    return m

#keyのデフォ値に無名関数lambda x:xを入れて常にkeyを使える形にする
#対象gから取り出した各要素iについてkey(i)を比べ大小関係によりiで答えmを書き換える


##########
