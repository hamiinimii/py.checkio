#checkio_TheMostWantedLetter

##########
#MyAnswer

import re
def checkio(text):

    tlist=list(re.sub(r'[^a-zA-Z]','',text.lower()))
    return sorted(sorted(tlist,reverse=True),key=tlist.count)[-1]    

    #1.2を応用。正規表現で英字以外を消した後、sortedを使って並べ替え。
    #sortedでアルファベット逆順に並べた後、countで数えて小さい順に整列。
    #一度目の整列をある程度保持するらしく、順番が入れ替わることなく答えにたどり着ける。

