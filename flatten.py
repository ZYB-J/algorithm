"""
输入一颗树，把树变成一条链表结构
"""
from tree import Tree


def flatten(root:Tree.Node):
    if root is None:
        return

    flatten(root.left)
    flatten(root.right)
    left = root.left
    right = root.right
    root.left = None
    root.right = left
    p = root
    while p.right:
        p = p.right
    p.right = right

def printResult(root):
    node = root
    while node:
        print(node.key)
        node = node.right


if __name__=='__main__':
    arr=[1,2,3,4,5,6]
    tree = Tree()
    tree.createTree(arr)
    #tree.preorderTraversal()
    flatten(tree.root)
    printResult(tree.root)