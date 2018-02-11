#checkio_SecreteMessage

##########
#MyAnswer

def find_message(text):

    ans=''.join(re.findall(r'[A-Z]',text))
    
    return ans

    #正規表現の検索で事足りた

