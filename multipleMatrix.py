"""
@version: 1
@author: zyb
@site: 
@software: PyCharm Community Edition
@file: multipleMatrix.py
@time: 2017/3/10 10:06
矩阵乘法运算
"""
def multipleMatrix(ma1,ma2,n):
    new_ma=[]

    for i in range(0,n):
        new_ma.append([])
        for j in range(0,n):
            temp = 0
            for k in range(0,n):
                temp=temp+ma1[i][k]*ma2[k][j]
            new_ma[i].append(temp)
    return new_ma

if __name__=="__main__":

    ma1=[[1,2],[1,2]]
    ma2=[[2,1],[2,1]]
    print(ma1)
    new_ma=multipleMatrix(ma1,ma2,2)
    print(new_ma)