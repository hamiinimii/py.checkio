#checkio_PawnBrotherfood
#coding:utf-8

##########
#MyAnswer

def safe_pawns(pawns):
    
    safelist=[]
    
    for i in pawns:
        for j in pawns:
            if abs(ord(j[0])-ord(i[0]))==1 and int(j[1])==int(i[1])+1:
                safelist.append(j)
                
    return len(set(safelist))

    #pawnの位置はa-hと1-8で表される。forループで一つpawnを選び、場のpawnがそれに守られているか調べている。
    #a-hの横座標に関して1マスずれであることを、ord('座標[0]')の差の絶対値==1で確認。
    #1-8の縦座標に対して1マスずれであることを、int('座標[1]')の差==1で確認。
    #安全だった場合、守られているポーンをその位置で呼称、safelistに格納。
    #最後、set(集合)にして重複をなくし、その要素数で安全なポーンの数を返す。

##########
#1

def get_saves(field):
    y = chr(ord(field[1]) + 1)
    x1 = chr(ord(field[0]) - 1)
    x2 = chr(ord(field[0]) + 1)
    return '%s%s' % (x1, y), '%s%s' % (x2, y)


def safe_pawns(pawns):
    save_counter = []
    for p in pawns:
        for c in get_saves(p):
            if pawns.__contains__(c) and not save_counter.__contains__(c):
                save_counter.append(c)
    return save_counter.__len__()


    #関数を二つ定義。一つ目(get_saves)では、引数の座標のpawnが守護ることのできる座標を文字列で導出する。
    #二つ目は、get_savesにpawnの各座標を代入、導出されたしょごされた座標にpawnがいるか調べる。
    #いた場合、かつ初出の場合（重複防止。集合の方がクレバー）、save_counterに格納。lenで答えとする。
    #クラスとかインスタンスとかはHomeだいたいクリアしてからもっかい教本読み直そうな。
  
##########
#2

##########
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
