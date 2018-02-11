#checkio_BetweenMarkers

##########
#MyAnswer

def second_index(text: str, symbol: str):
    
    try:
        ans=text[text.find(symbol)+1:].index(symbol)+text.find(symbol)+1
    except:
        ans=None
    return ans

