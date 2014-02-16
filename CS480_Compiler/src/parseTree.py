'''
Created on Feb 5, 2014

@author: mr_hickman
'''
class ParseTree:
    def __init__(self, rootNode):
        self.root = rootNode
        self.currentNode = rootNode
        self.currentChild = [-1]
        self.currentChildCount = [rootNode.getChildCount()]

    def getNextLeftMostNode(self):
        if self.currentNode:
            while self.currentChildCount[-1] != 0 and self.currentChild[-1] + 1 < self.currentChildCount[-1] :
                self.currentChild[-1] += 1 
                self.currentNode = self.currentNode.getChild(self.currentChild[-1])
                self.currentChild.append(-1)
                self.currentChildCount.append(self.currentNode.getChildCount())
                
            leftMost = self.currentNode
            self.currentNode = self.currentNode.getParent()
            self.currentChild.pop()
            self.currentChildCount.pop()
            return leftMost
        else:
            # Is finished
            return '' 
