#checkio_CurrencyStyle

#unsolved

import re

def checkio(text):
    strlist=text.split(' ')
    for i,x in enumerate(strlist):
        if (x[:-1].find(',') if x[:-1].rfind(',')>-1 else len(x))>x[:-1].rfind('.'):
            x = re.sub(',', 'C', x)
            print(x)
            print(bool(re.fullmatch('[0-9][0-9][0-9][C]*',x[x.rfind('.')+1:])))
            x = re.sub('\.', ',', x) if (re.fullmatch('[0-9][0-9][0-9][C]*',x[x.rfind('.')+1:]) and len(x[x.rfind('.')+1:])<4)\
            else re.sub('\.', ',', x[:x.rfind('.')])+x[x.rfind('.'):]
            print(x)
            x = re.sub('C', '.', x)
            x = x[:-1] + ',' if x[-1] == '.' else x
            strlist[i] = x

    print(' '.join(strlist))
    return ' '.join(strlist)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("$1.234.567,89") == "$1,234,567.89", "1st Example"
    assert checkio("$0,89") == "$0.89", "2nd Example"
    assert checkio("Euro Style = $12.345,67, US Style = $12,345.67") == \
           "Euro Style = $12,345.67, US Style = $12,345.67", "European and US"
    assert checkio("Us Style = $12,345.67, Euro Style = $12.345,67") == \
           "Us Style = $12,345.67, Euro Style = $12,345.67", "US and European"
    assert checkio("$1.234, $5.678 and $9") == \
           "$1,234, $5,678 and $9", "Dollars without cents"
    assert checkio("$5.34") == \
           "$5.34", "Dollars with cents"