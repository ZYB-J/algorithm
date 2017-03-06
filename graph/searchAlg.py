"""
@version: 1
@author: zyb
@site: 
@software: PyCharm Community Edition
@file: searchAlg.py
@time: 2016/6/24 9:47
"""
class DepthFirstSearch(object):

    def __init__(self,g,v):
        self.marked = []
        self.edgeTo = []
        for i in range(0,g.getVerticals()):
            self.marked.append(False)
            self.edgeTo.append(-1)
        self.count = 0
        self.s = v
        self.dfs(g,v)


    def dfs(self,g,v):
        self.marked[v]=True;
        #self.marked[v]=True
        print(self.count,'---------')
        self.count=self.count+1
        for vertical in g.getAdjacency(v):
            if not self.marked[vertical]:
                self.edgeTo[vertical]=v
                self.dfs(g,vertical)

    def isMarked(self,vertical):
        return self.marked[vertical]

    def count(self):
        return self.count

    def hasPathTo(self,v):
        return self.marked[v]

    def pathTo(self,v):
        if not self.hasPathTo(v):
            return None
        path=[]
        i=self.edgeTo[v]
        path.append(v)
        while i!=self.s:
            path.append(i)
            i=self.edgeTo[i]

        return path
from graph import  Graph
if __name__=='__main__':
    g = Graph(6);
    g.addEdge(0, 2)
    g.addEdge(0, 1)
    g.addEdge(0, 5)

    g.addEdge(2,1)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 4)
    g.addEdge(3, 5)

    dfs = DepthFirstSearch(g,0)
    pat = dfs.pathTo(5)
    print( pat)
    st=''
    for i in range(0,len(pat)):
        st+=str(pat.pop())

    print(st)
    print(g.adjacency)