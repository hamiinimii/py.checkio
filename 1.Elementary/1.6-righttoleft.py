#checkio_RightToLeft

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
