"""
四个滚动轮的锁，给定一个集合['0000','1001'],给定一个解'1000'
如果滚动轮的过程锁数字包含在集合中元素，锁就锁死了
得到解最少步骤
"""

target = '2003'
limitSet={'2001','3003','3000'}
visit = {'0000'}

start = '0000'
queue = [(start,0)]

def findMinStep():
    step = 0
    while(len(queue)>0):
        item,depth = queue.pop(0)
        if item == target:
            return depth
        for i in range(0,4):
            num = int(item[i])
            for d in(-1,1):
                y = (num + d) % 10
                newItem = createNewItem(item,i,y)
                if newItem not in visit:
                    queue.append((newItem,depth+1))
                    visit.add(newItem)
        step = step + 1

    return -1

def createNewItem(oldItem:list,index,num):
    s = ''
    for i in range(0,4):
        if i != index:
            s = s+oldItem[i]
        else:
            s = s+str(num)
    print(s)
    return s
if __name__=='__main__':
    print(start[0])
    print(findMinStep())

