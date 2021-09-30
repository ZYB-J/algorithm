"""
从一个数组中构造一颗最大二叉树
根节点是最大值
左子节点是最大值左边的数组构成的最大二叉树
右子节点是最大值右边数组构成的最大二叉树
"""

from tree import Tree

def constructMaxBinaryTree(arr:list):
    if len(arr) == 0:
        return None
    maxValueIndex = -1
    maxValue = 0
    for index,value in enumerate(arr):
        if maxValue<value:
            maxValue = value
            maxValueIndex = index

    node = Tree.Node(maxValue)
    node.left = constructMaxBinaryTree(arr[0:maxValueIndex])
    node.right = constructMaxBinaryTree(arr[maxValueIndex+1:])

    return node










if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    #print()
    root = constructMaxBinaryTree(arr)
    tree = Tree()
    tree.root  = root
    print(tree.preorderTraversal())
