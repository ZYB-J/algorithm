"""
@version: 1
@author: zyb
@site: 
@software: PyCharm Community Edition
@file: binarytree.py
@time: 2016/4/29 11:50
"""

class Binarytree(object):
    def __init__(self):
        self.root=None
    class Node(object):
        def __init__(self,key,value, num):
            self.key=key
            self.value=value
            self.num=num
            self.left=None
            self.right=None

#递归方式
    def get(self,key):
        node=self.root
        val=0
        while node:
            if key>node.key:
                node=node.right
            elif key<node.key:
                node=node.left
            else:
                val=node.value
                break
        return val

    def putNode(self, node, key, value):
        if node == None:
            return Binarytree.Node(key, value,1)
        if key<node.key:
            node.left=self.putNode(node.left,key,value)
        elif key>node.key:
            node.right=self.putNode(node.right,key,value)
        else:
            node.value=value
        node.num=self.size(node.left)+self.size(node.right)+1
        return node

    def size(self,node):
        if node==None:
            return 0
        else:
            return node.num

    def put(self,key,value):
        self.root=self.putNode(self.root,key,value)

    def printTree(self):
        self.printValue(self.root)

    def printValue(self,node):
        #node = self.root
        if node.left!=None:
            self.printValue(node.left)
        print(node.key)
        if node.right!=None:
             self.printValue(node.right)


    def getMax(self):
        node=self.root
        while node.right:
            node = node.right
        maxval=node.key
        return maxval

    def getMin(self):
        node=self.root
        while node.left:
            node=node.left
        return node.key

    def delete(self,key):
        self.root=self._deleteKey_(self.root,key)

    def _deleteKey_(self,node,key):
        if key > node.key:
            node.right=self._deleteKey_(node.right,key)
        elif key<node.key:
            node.left=self._deleteKey_(node.left,key)
        else:
            if node.left==None:
                return node.right
            elif node.right==None:
                return node.left
            else:
                t=node
                node=self.getMinNode(node.right)
                node.right=self.delMinKey(t.right)
                node.left=t.left
        node.num=self.size(node.left)+self.size(node.right)+1
        return node
        pass

    def getMinNode(self,node):
        if node.left==None:
            return node
        else:
            return self.getMinNode(node.left)
    #删除最小值
    def delMin(self):
         self.root=self._delMinKey(self.root)

    def _delMinKey(self,node):
        if node.left==None:
            return node.right
        node.left=self._delMinKey(node.left)
        node.num=self.size(node.left)+self.size(node.right)+1
        return node

    def preorderTraversal(self,node:Node):
        stack=[]
        while node or len(stack)>0:
            while node:
                print(node.key,end=" ")
                stack.append(node)
                node = node.left

            if len(stack)>0:
                node = stack.pop()
                node = node.right

    def middleorderTraversal(self,node:Node):
        stack = []
        while node or len(stack):
            while node:
                stack.append(node)
                node = node.left

            if len(stack):
                #self.printStack(stack)
                #print()
                node = stack.pop()
                print(node.key, end=" ")
                node = node.right

    def postorderTraversal(self,node:Node):
        stack = []
        lastNode = node
        while node or len(stack):
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is None or node.right==lastNode:
                node = stack.pop()
                print(node.key,end=" ")
                lastNode = node
                node = None
            else:
                node = node.right
    def printStack(self,stack):
        for i in stack:
            print(i.key,end=" ")

if __name__=='__main__':
    tree = Binarytree()
    tree.put(6,6)
    tree.put(4, 10)
    tree.put(1, 11)
    tree.put(2, 11)
    tree.put(5, 5)
    tree.put(7, 5)
    #tree.printTree()
    tree.preorderTraversal(tree.root)
    print()
    tree.middleorderTraversal(tree.root)
    print()
    tree.postorderTraversal(tree.root)
    # print('1:',tree.get(1))
    # print('44:',tree.get(44))
    # print('max:',tree.getMax())
    # print('min:',tree.getMin())
    # tree.delete(4)
    # tree.printTree()
    l = [1,2,4]
    #print(l[-1])
