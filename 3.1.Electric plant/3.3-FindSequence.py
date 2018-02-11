#checkio_Brackets

##########
#MyAnswer

from itertools import product as prd

def checkio(matrix):

    N = len(matrix[0])
    num = [0,0]
    cnt = {'V': 0, 'H': 0, 'D1': 0, 'D2': 0}

    # vertical and horizontal
    for i in range(N):
        for j in range(N):
            if num[0] == matrix[j][i]:
                cnt['V'] += 1
            else:
                cnt['V'] = 0
                num[0]=matrix[j][i]
            if num[1] == matrix[i][j]:
                cnt['H'] += 1
            else:
                cnt['H']=0
                num[1]=matrix[i][j]
            if cnt['V'] == 3 or cnt['H'] == 3:
                return True
        cnt['V'] = 0
        cnt['H'] = 0
        num = [0,0]

    # diagonal
    for i in prd(range(N),range(N)):
        for j in range(N):
            if i[0] + j < N and i[1] + j < N:
                if num[0] == matrix[i[0] + j][i[1] + j]:
                    cnt['D1'] += 1
                else:
                    cnt['D1'] = 0
                    num[0] = matrix[i[0] + j][i[1] + j]
                if cnt['D1'] == 3:
                    return True

            if i[0] + j < N and i[1] - j >=0:
                if num[1] == matrix[i[0] + j][i[1] - j]:
                    cnt['D2'] += 1
                else:
                    cnt['D2'] = 0
                    num[1] = matrix[i[0] + j][i[1] - j]
                if cnt['D2'] == 3:
                    return True
        cnt['D1'] = 0
        cnt['D2'] = 0
        num = [0,0]
        
    return False


##########
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
       [1,1,2,4,6,4,1,4],
       [3,3,4,9,9,1,9,9],
       [2,6,7,2,7,8,8,8],
       [5,7,8,6,5,6,3,1],
       [7,7,4,4,1,7,8,1],
       [2,5,7,9,7,5,8,6],
       [1,5,3,7,2,1,6,3],
       [1,1,3,7,7,4,9,7]
    ]) == True, "Diagonal"

