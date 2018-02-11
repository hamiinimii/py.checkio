#checkio_Brackets
#coding:utf-8

##########
def reverse_roman(rst):

    roman={'CM':900,'M':1000,'CD':400,'D':500,'XC':90,'C':100,'XL':40,'L':50,\
    'IX':9,'X':10,'IV':4,'V':5,'I':1}
    
    for i in roman:
        rst=rst.replace(i,str(roman[i])+'+')
    
    return eval(rst+'0')

##########
#1

reverse_roman=lambda n,f='IVXLCDM'.index:sum((1,5)[f(i)%2]*10**(f(i)//2)*(-1,1)[f(i)>=f(j)]for i,j in zip(n,n[1:]+n[-1]))



##########
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');