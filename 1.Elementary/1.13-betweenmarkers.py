#checkio_BetweenMarkers
#coding:utf-8

##########
#MyAnswer

def between_markers(text: str, begin: str, end: str) -> str:
    
    
    if text.find(end)>text.find(begin):
        half=text[:text.index(end)]
    elif text.find(end)==-1:
        half=text
    else:
        half=''
        
    try:
        ans=half[half.index(begin)+len(begin):]
    except:
        ans=half

        
    return ans

##########
#2

def between_markers(text: str, begin: str, end: str) -> str:
        
    
    start, blen, finish = 0,0, len(text)
   
    if text.find(begin)>= 0 :
        start = text.index (begin)
        blen= len(begin)
    if text.find(end) > 0:
        finish = text.index (end)
    
    return (text[start+blen:finish])

    #strのスライスはindex指定が逆になると空strを返す。なのでmarkerが前後していたらそのまま記述すれば良い。
    #blen=begin length

##########
#3

def suppressed(f):
    from contextlib import suppress
    def wrapper(*args, **kwargs):
        with suppress(Exception):
            return f(*args, **kwargs)
    return wrapper

    #あとで考える。

##########


#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
