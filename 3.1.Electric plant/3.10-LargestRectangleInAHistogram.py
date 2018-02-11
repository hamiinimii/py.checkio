#checkio_Brackets

##########
#MyAnswer

def largest_histogram(histogram):
 
    cnt=[0]
    rect=[]
    for i in range(1,max(histogram)+1):
        for j in histogram:
            if i<=j:
                cnt[-1]+=1
            else:
                cnt.append(0)
        rect.append(max(cnt)*(i))
        cnt=[0]
        
    return max(rect)

#高さの低い順に探す


##########
#Error

import re
def largest_histogram(h):
        
    maxwide=lambda h:len(max(str(h).strip('[\[\]]').replace(', ','').split('0'), key=len))

    mxr=[]
    for i in range(1,max(h)+1):
        mxr.append(maxwide(h)*i)
        for j in range(len(h)):
            h[j]-=1
            print(h)

    return(max(mxr))

#0以下になった場合を除けないなど問題多数。

##########



if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
