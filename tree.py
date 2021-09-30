class Tree(object):
    def __init__(self):
        self.root=None
    class Node(object):
        def __init__(self,key):
            self.key=key
            self.left=None
            self.right=None


    def createTree(self,arr):
        self.root = Tree.Node(arr[0])
        count = 0
        length = len(arr)
        node = self.root
        nodeArr = []
        nodeArr.append(node)
        while count<=length/2 and node is not None:
            left = count*2+1
            right = left+1
            if left<length:
                node.left = Tree.Node(arr[left])
                nodeArr.append(node.left)
            if right < length:
                node.right = Tree.Node(arr[right])
                nodeArr.append(node.right)
            count = count+1
            node = nodeArr[count]
    def preorderTraversal(self):
        node = self.root
        stack=[]
        result = []
        while node or len(stack)>0:
            while node:
                result.append(node.key)
                stack.append(node)
                node = node.left

            if len(stack)>0:
                node = stack.pop()
                node = node.right
        return result
    def middleorderTraversal(self):
        stack = []
        result = []
        node = self.root
        while node or len(stack):
            while node:
                stack.append(node)
                node = node.left

            if len(stack):
                node = stack.pop()
                result.append(node.key)
                node = node.right
        return result
    def printTree(self,root):
        if root:
            print(root.key,end=" ")
            self.printTree(root.left)
            self.printTree(root.right)



if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    tree = Tree()
    tree.createTree(arr)
    tree.preorderTraversal()
    #print()
    #tree.printTree(tree.root)
