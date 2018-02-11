#checkio_RightToLeft

##########
#MyAnswer

def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    try:
        return array[n]**n
    except:
        return -1

