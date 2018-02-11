#checkio_FizzBuzz
#coding:utf-8

##########
#MyAnswer

def checkio(number):
    
    ans=''
    check=0
    if number%3==0:
        ans+='Fizz'
        check=1
    if number%5==0:
        if check:
            ans+=' '
        ans+='Buzz'
    
    return ans if ans else str(number)


##########
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
