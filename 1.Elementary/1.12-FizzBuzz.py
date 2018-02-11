#checkio_FizzBuzz

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

