#checkio_RightToLeft
#coding:utf-8

##########
#MyAnswer

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    words=','.join(list(phrases))
    ans=words.replace('right','left')
    #replaceは放っておいても全部置換してくれるのでmapでばらまく等しなくて良い

    return ans

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

##########
#1

def left_join(phrases):
    result = ''
    for word in phrases:
        while word.count('right'):
            word = word[:word.find('right')]+'left'+word[word.find('right')+5:]
        result += word+','
    return result[:-1]

    #区切られている文字列をforで一つずつ抽出（word）。rightが含まれていた場合、rightの位置の一個前と後を別々に取り出し、間にleftを挟む。なお、ここで扱われている文字列wordに対しての処理は、1文字ずつに対して行われている。
    #resultに','と一緒に足していく形で格納。

##########
