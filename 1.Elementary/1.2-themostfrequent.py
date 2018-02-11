#checkio_theMostFrequent

def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    cnt_o=1 #count_old 要素が２種類以上の時、1種類前の要素の数のメモリ
    
    #要素1個の場合の例外処理
    if len(data)==1:
        ans=data[0]
    #2個以上（not2種類以上でも可）の時判定
    else:
        while data!=[]: 
            cnt_n=1
            target=data[0]
       
            for i in range (1, len(data)): #rangeは末端の数の一個小さいのまでだった。だからlenでおk
                if data[0]==data[i]:
                    cnt_n=cnt_n+1
            else:
                for j in range (cnt_n):
                    data.remove(target)
                else:
                    if cnt_o<cnt_n:
                        cnt_o=cnt_n
                        ans=target
                #elif cnt_o==cnt_n:
                #    ans.append(target)
    
    return ans

