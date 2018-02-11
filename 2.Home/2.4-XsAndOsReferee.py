#checkio_XsAndOsReferee
#coding:utf-8

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


##########
#1

def checkio(game_result):
    verticals = []
    diagonal = ''
    for i in range(3):
        value = ''
        for a in range(3):
            value += game_result[a][i]
            diagonal += game_result[a][i] if a==i else ''
        verticals.append(value)
    diagonals=[game_result[0][2] + game_result[1][1] + game_result[2][0], diagonal]
    result_all = diagonals + verticals + game_result
    return 'X' if 'XXX' in result_all else 'O' if 'OOO' in result_all else 'D'

    #結果中の三連箇所を全てresult_allに格納。横は既にgame_result中にある。
    #縦(verticals)と斜め(diagonal)をまとめるのに、２段forループを使う。先に列を指定、次に行。
    #縦は内ループ一回ごとに取り出して格納、左斜めは3回の外ループの中で辿っていく。
    #右斜めはループで辿りにくいので別に手動で辿る。
    #最後に、三連箇所を一つの文字列としてリストでまとめたresult_allから該当を探し出す。

##########
#2

def checkio(game_result):

    #adding verticals
    game_result.append((game_result[0][0] + game_result[1][0] + game_result[2][0]))
    game_result.append((game_result[0][1] + game_result[1][1] + game_result[2][1]))
    game_result.append((game_result[0][2] + game_result[1][2] + game_result[2][2]))
    

    #adding diagonals
    game_result.append((game_result[0][0] + game_result[1][1] + game_result[2][2]))
    game_result.append((game_result[0][2] + game_result[1][1] + game_result[2][0]))
    
    if 'XXX' in game_result:
        return 'X'
    
    if 'OOO' in game_result:
        return 'O'
    
    return 'D'  

    #見た目はこっちのがスマート。game_resultに縦及び斜めで辿ったものを追加していき、勝者が存在するかを判定。

##########
#3

import re

def checkio(game_result):
    winning =  ("XXX......",
                "...XXX...",
                "......XXX",
                "X..X..X..",
                ".X..X..X.",
                "..X..X..X",
                "X...X...X",
                "..X.X.X..")
    game = "".join(game_result)
    for w in winning:
        if re.match(w, game):
            return "X"
        if re.match(w.replace("X", "O"), game):
            return "O"
    return "D"

    #面白い。全部繋げた上でパターンを全て書き出してmatchを調べる。Xを調べたらOに移って調べる。

##########



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "XXX",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

