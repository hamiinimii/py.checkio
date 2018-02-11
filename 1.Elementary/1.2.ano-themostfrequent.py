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


