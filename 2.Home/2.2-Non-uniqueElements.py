#checkio_TheMostWantedLetter
#coding:utf-8

##########
#MyAnswer

def checkio(data):
    
    for i in data[:]:
        if data.count(i)==1:
            data.remove(i)
    
    return data    
    

##########
#1

    return data.remove(uni for uni in data if data.count(uni)==1)
    #return [k for k in data if data.count(k)>1]
    #return [data.remove(k) for k in [uni for uni in data if data.count(uni)==1]]
    
##########
#2

##########
if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
    
    
