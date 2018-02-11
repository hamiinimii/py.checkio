#checkio_PawnBrotherfood

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

