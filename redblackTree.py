"""
@version: 1
@author: zyb
@site: 
@software: PyCharm Community Edition
@file: redblackTree.py
@time: 2016/5/5 9:57
"""
class rbTree(object):
    RED=True
    BLACK=False

    def __init__(self):
        self.root = None

    class Node(object):
        def __init__(self,key,value,number,color):
            self.key = key
            self.value = value
            self.number = number
            self.color = color
            self.left = None
            self.right = None


    def isRed(self ,node):
        if node==None:
            return False
        return node.color == rbTree.RED

    def get(self, key):
        node = self.root
        val = 0
        while node:
            if key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left
            else:
                val = node.value
                break
        return val
    #左旋
    def ratateLeft(self,node):
        x=node.right
        node.right=x.left
        x.left=node
        x.color=node.color
        node.color=rbTree.RED
        return x

    #右旋
    def ratateRight(self,node):
        x=node.left
        node.left=x.right
        x.right=node
        x.color=node.color
        node.color=rbTree.RED
        return x

    def put(self,key,value):
        self.root=self.putN(self.root,key,value)
        self.root.color = rbTree.BLACK

    def putN(self,node,key,value):
        if node==None:
            return self.Node(key,value,1,rbTree.RED)
        if key<node.key:
            node.left = self.putN(node.left,key,value)
        elif key>node.key:
            node.right=self.putN(node.right,key,value)
        else:
            node.value=value

        if self.isRed(node.right) and not self.isRed(node.left):
            node=self.ratateLeft(node)
        if self.isRed(node.left) and self.isRed(node.left.left):
            node=self.ratateRight(node)
        if  self.isRed(node.left) and self.isRed(node.right):
            node = self.flipColor(node)

        node.number=self.size(node.left)+self.size(node.right)
        return node

    def flipColor(self,node):
        node.left.color=rbTree.BLACK
        node.right.color=rbTree.BLACK
        node.color=rbTree.RED
        return node

    def size(self, node):
        if node == None:
            return 0
        else:
            return node.number

    def printTree(self):
        self.printValue(self.root)

    def printValue(self, node):
        # node = self.root
        if node.left != None:
            self.printValue(node.left)
        print(node.key)
        if node.right != None:
            self.printValue(node.right)

if __name__=='__main__':
    tree=rbTree()
    tree.put(3, 6)
    tree.put(4, 10)
    tree.put(1, 11)
    tree.put(5, 5)
    tree.put(2, 5)
    tree.put(10, 5)
    tree.printTree()