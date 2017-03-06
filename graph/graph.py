"""
@version: 1
@author: zyb
@site: 
@software: PyCharm Community Edition
@file: graph.py
@time: 2016/6/23 15:51
"""
class Graph(object):
    def __init__(self,vertical):
        self.vertical = vertical
        self.edge=0
        self.adjacency=[]
        for i in range(0,vertical):
            self.adjacency.append([])


    def getVerticals(self):
        return self.vertical

    def getEdges(self):
        return self.edge

    def addEdge(self,verticalStart,verticalEnd):
        self.adjacency[verticalStart].append(verticalEnd)
        self.adjacency[verticalEnd].append(verticalStart)
        self.edge+=1

    def getAdjacency(self,vertical):
        return self.adjacency[vertical]

