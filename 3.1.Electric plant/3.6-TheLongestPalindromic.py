#checkio_TheLongestPalindromic

##########
#MyAnswer

def longest_palindromic(text):
    
    palF=''
    ans=''
    
    for i in range(len(text)):
        temp=text[i:]
        for j,x in enumerate(temp):
            palF=x+palF
            if palF==temp[:j+1] and len(palF)>len(ans):
                ans=palF
        palF=''

    return ans

#回文候補の、初めの文字を引数の1番目から指定するループ。
#初めの文字以降の全てを、順にpalFの先頭に付加し、逆文字列を作る。
#その上で、逆文字列が元文字列の付加したところまでと一致するか確認。


##########
if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"


