#checkio_TheLongestPalindromic
#coding:utf-8

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
#1

longest_palindromic = lambda inp: "".join(next(t for n in range(len(inp), 0, -1) for t in zip(*(__import__("itertools").islice(inp, i, None) for i in range(n))) if t == t[::-1]))                

#ちょっと理解できないから待って。
#なんか前後に相互に参照してるっぽくてますます意味わからん。みおん帰る。


##########
#2

longest_palindromic=l=lambda t:t*(t==t[::-1])or max(l(t[:-1]),l(t[1:]),key=len) 

#こっちは理解できた。テキストが回文かのT/Fをかけることで回文ならテキストを返し、非回文ならorで前後一文字ずつ減らして再帰させる。うまい。回文は再帰でやるのだと読んだことはあったがこうやるのか。

##########
if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"


