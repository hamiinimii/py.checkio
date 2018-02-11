#checkio_SecreteMessage
#coding:utf-8

##########
#MyAnswer

def find_message(text):

    ans=''.join(re.findall(r'[A-Z]',text))
    
    return ans

    #正規表現の検索で事足りた

##########
#1

def find_message(text):

    ans=''.join(filter(lambda x: x.isupper(),text))

    return ans

    #filterでisupperを拡散する波動。次のように書いてもいける

    #ans=''.join(filter(str.isupper, text))

##########

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

