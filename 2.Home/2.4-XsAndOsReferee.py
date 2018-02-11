#checkio_XsAndOsReferee

##########
#MyAnswer

def checkio(gr):
    
    winner="D"
    
    #horizontal
    for i in gr:
        if i[0]==i[1] and i[0]==i[2] and i[0]!=".":
            winner=i[0]
    
    #vertical
    for i in range(3):
        if gr[0][i]==gr[1][i] and gr[0][i]==gr[2][i] and gr[0][i]!=".":
            winner=gr[0][i]
            
    #diagonal
    if gr[1][1]==gr[0][0] and gr[1][1]==gr[2][2] and gr[1][1]!=".":
        winner=gr[1][1]
    if gr[1][1]==gr[0][2] and gr[1][1]==gr[2][0] and gr[1][1]!=".":
        winner=gr[1][1]
    
    return winner


##########
#ERROR
def checkio(game_result):
    
    winner="D"
    #horizontal
    for i in range(3):
        for j in game_result[i]:
            if j[0]==j[1] and j[0]==j[2]:
                winner=i[0]

    #(途中)
    #jの指定で、一見文字列のリストgame_resultから文字列を取り出しているように見えるかもしれないが、
    #よく見ると、game_result[i]というリストの1要素の1文字列から、jで一文字ずつ取り出している。
    #ので、out of rangeのエラーが出る。1文字の文字列に1番目2番目はないからだ。

