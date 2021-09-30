
"""
回溯算法
八皇后问题
"""

length = 8
result = [-1,-1,-1,-1,-1,-1,-1,-1]
counter = [0]
def callQueen(row:int):
    if row == 8:
        printQueen()
        counter[0] = counter[0]+1
        print("999")
        return
    for column in range(0,8):
        if isOk(row,column):
            result[row]=column
            #print(row,column)
            callQueen(row + 1)
        else:
            print(row,column)

def isOk(row:int,column:int):
    left = column-1
    right = column+1
    for i in range(row-1,-1,-1):
        if result[i] == column:
            return False
        if left>=0:
            if result[i] == left:
                return False
        if right<8:
            if result[i] == right:
                return False
        left = left -1
        right = right+1

    return True


def printQueen():
    for i  in range(0,8):
        for j in range(0,8):
            if j == result[i]:
                print(i,end=" ")
            else:
                print("*",end=" ")
        print("")
    print("------------------------")

if __name__=='__main__':
    arr=[10,1,-4,3,-4]
    callQueen(0)
    print(counter)
