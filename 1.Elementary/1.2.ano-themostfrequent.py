#coding:utf-8
#checkio_theMostFrequent

##############
#1

def most_frequent(data):
    c = dict() #辞書を定義
    for s in data: #dataの一つ一つを取り出して処理する
        c[s] = c.get(s, 0) + 1
        #getは辞書の指定キーの値を返す。dict.get(key,dafault=None) 
        #dafaultの値は、キー値が利用できない時に返す値。今回はdefaultを0に設定している。
        #forループで前から順に、各要素をキーにして、出てきた回数をキー値に足していく。
    return max(c.items(), key=lambda x: x[1])[0]
        #maxは最大値を取り出す。ここで引数keyはキーワード引数、順序付けの関数を指定できる。例えば文字列化など。
        #今回は無名関数lambdaでx[1]、つまり辞書のアイテムの各2番目の要素（つまりキー値部分）を指定。
        #その上で、maxはキーとキー値をセットにして返す。その[0]つまり1番目、キーを返す。

##############
#2

def most_frequent(data):
    
    return sorted(data,key=lambda s: data.count(s),reverse=True)[0]
    #１行でまとめてきやがった。
    #sorted:ソート。keyパラメータにcountで個数を返し、reverseで降順に。
    #よって多い順に並ぶことになる。その最も先頭[0]にあるものは最も数が多いもの。


##############
#3

def most_frequent(lst):
    return max(set(lst), key=lst.count)
    #1行。setは集合（順番、要素重複なし）。集合にした上で「最大」を元データでの個数にする。    
        
##############
#4

def most_frequent(data):
  y = [(data.count(x),x) for x in data]
  return (sorted(y)[-1])[1]
  #リスト内包表記。data内での数とデータ要素を並べたものを並べる構造を作り、
  #ソートで最末端（個数最大）の2番目（要素そのもの）を取り出す。

##############

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c', 
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')

