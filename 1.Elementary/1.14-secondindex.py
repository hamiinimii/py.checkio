#checkio_BetweenMarkers
#coding:utf-8

##########
#MyAnswer

def second_index(text: str, symbol: str):
    
    try:
        ans=text[text.find(symbol)+1:].index(symbol)+text.find(symbol)+1
    except:
        ans=None
    return ans


##########
#1

def second_index(text, sym):
    return None if text.count(sym) < 2 else text.find(sym, 1 + text.find(sym))


##########
#2


##########


#These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
