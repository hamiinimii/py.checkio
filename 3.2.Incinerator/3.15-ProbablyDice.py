#checkio BirdLanguage
#coding:utf-8

##########
#MyAnswer

def probability(dice_number, sides, target):
    
    deno=sides**dice_number
    if sides*dice_number<target:
        return 0
    
    cnt=0
    sum_old={0:1}
    while cnt<dice_number:
        cnt+=1
        sum_new={}
        for i in range(sides):
            for j in sum_old:
                if not j+(i+1) in sum_new:
                    sum_new[j+(i+1)]=0
                sum_new[j+(i+1)]+=sum_old[j] if target-(dice_number-cnt)*sides<=j+(i+1)<=target else 0
        
        sum_old=sum_new

    nume=sum(sum_old.values())
    return nume/deno

#Inadequate answer 2のコメントに書いたことをした。
#たしていって同じ数になったものを、辞書に 和:個数 で記録し、計算を削減。格段に早くなったっぽい。


##########
#1

def probability(n,s,t):
    p = [1]+[0]*n*s #和の個数を格納するリストを作っている。indexが和に対応
    for d in range(n): #ダイス個数分以下の処理を繰り返す。つまりダイスを一個ずつ振っていく。
        for i in range(n*s,-1,-1):
            p[i] = sum(p[i-j-1] for j in range(s) if i>j)/s
            #和iの確率は、和から出目を引いたもの（ただし差が1以上に限るのは当然）の確率（つまり１ダイスロール前の和の確率）の合計
            #毎回全可能性（ありうる最大和から下へ）を辿るが、まだ生じ得ない和は一個前が0なので今も0になるだけ。
            #そして上から辿るのは、上和は下和へ絶対に影響しないため。
    return p[t] if t<=n*s else 0 #最後にtarget以上の場合を除外しているが、
    #行数は増えても最初に持って来た方が処理は減るよな。

##########
#Inadequate answer

from itertools import product
def probability(dice_number, sides, target):
    
    nume=deno=0
    for j in product([i+1 for i in range(sides)],repeat=dice_number):
        deno+=1
        nume+=1 if sum(j)==target else 0
    
    return nume/demo

#とりあえず正解っぽい（保証はないがサンプルは全てクリアした）けど、総当たりなのでクソ重い。

##########
#Inadequate answer 2

def probability(dice_number, sides, target):
    
    deno=sides**dice_number
    if sides*dice_number<target:
        return 0
    
    cnt=0
    sum_old=[0]
    while cnt<dice_number:
        cnt+=1
        sum_new=[]
        for i in range(sides):
            for j in sum_old:
                sum_new+=[j+(i+1)] if target-(dice_number-cnt)*sides<=j+(i+1)<=target else []
        sum_old=sum_new

    nume=len(sum_old)   

    return nume/deno

#出目をたすその都度、今後どんなに目が良くてもtargetにたどり着けない和とtargetを超えた和を取り除いて来た。
#それでもまだ処理量が多すぎるらしい。次は同じ数の和を一つにまとめてみる。

##########
if __name__ == '__main__':
    #These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision
        
#    assert(almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
#    assert(almost_equal(probability(2, 6, 4), 0.0833)), "More points"
#    assert(almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
#    assert(almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
#    assert(almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
#    assert(almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
#    assert(almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"

