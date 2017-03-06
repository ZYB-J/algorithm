"""
@version: 1
@author: zyb
@site:
@software: PyCharm Community Edition
@file: skiplist.py
@time: 2017/2/21 16:45
跳跃表
"""
import math,random
class node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next=None
MAX_L=1;#初始最大长度
head=node(0,0)#初始头结点

def generateRandom():
   val = random.randrange(0,1)
   count=0
   while val==0:
       count=count+1
   if MAX_L>count:
        count=count
   else:
        count=MAX_L
   return count

def insertNode(node):
    level=generateRandom()




if __name__=="__main__":
    print(math.ceil(5/2))