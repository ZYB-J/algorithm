"""
根据先序/中序 遍历结果还原二叉树
"""
from tree import Tree



def restoreTree(predorderArr:list,inorderArr:list):
    size = len(predorderArr)
    return build(preorderArr,inorderArr,0,size,0,size)


def build(preorderArr:list,inorderArr:list,preStart:int,preEnd:int,inStart:int,inEnd:int):
    if preStart>=preEnd:
        return None

    key =  preorderArr[preStart]

    index = 0
    for i in range(inStart,inEnd):
        if inorderArr[i] == key:
            index = i
            break
    root = Tree.Node(key)
    leftSize = index-inStart
    root.left = build(preorderArr,inorderArr,preStart+1,preStart+leftSize+1,inStart,index)
    root.right = build(preorderArr,inorderArr,preStart+leftSize+1,preEnd,index+1,inEnd)
    return root

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    tree = Tree()
    tree.createTree(arr)
    preorderArr = tree.preorderTraversal()
    inorderArr = tree. middleorderTraversal()
    print(preorderArr)
    print(inorderArr)

    tree.root = restoreTree(preorderArr,inorderArr)
    print(tree.preorderTraversal())

