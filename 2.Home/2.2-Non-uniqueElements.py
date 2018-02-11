#checkio_TheMostWantedLetter

##########
#MyAnswer

def checkio(data):
    
    for i in data[:]:
        if data.count(i)==1:
            data.remove(i)
    
    return data    

