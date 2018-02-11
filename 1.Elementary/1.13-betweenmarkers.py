#checkio_BetweenMarkers

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


