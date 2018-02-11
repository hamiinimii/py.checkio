#checkio_ThreeWords

##########
#MyAnswer

def checkio(words):
    
    cnt=0
    wl=list(words)
    #「' 'の前後に文字がある」を連続して2回。
    while (cnt<2 and ' ' in wl):
        if (wl[wl.index(' ')-1].isdigit()==False\
        and wl[wl.index(' ')+1].isdigit()==False):
            cnt+=1
            print(cnt)
        else:
            cnt=0
        wl.remove(' ')
            
    return True if cnt==2 else False
    

