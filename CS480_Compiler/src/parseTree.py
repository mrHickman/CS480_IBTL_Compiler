'''
Created on Feb 5, 2014

@author: mr_hickman
'''
from parseNode import ParseNode
from token import Token

class ParseTree:
    def __init__(self, rootNode):
        self.root = rootNode
        self.currentNode = rootNode
        self.currentChild = [-1]
        self.currentChildCount = [rootNode.getChildCount()]
        self.leftMost = ''

    def getNextLeftMostNode(self):
        if self.currentNode:
            while self.currentChildCount[-1] != 0 and self.currentChild[-1] + 1 < self.currentChildCount[-1] :
                self.currentChild[-1] += 1 
                self.currentNode = self.currentNode.getChild(self.currentChild[-1])
                self.currentChild.append(-1)
                self.currentChildCount.append(self.currentNode.getChildCount())
                
            self.leftMost = self.currentNode
            self.currentNode = self.currentNode.getParent()
            self.currentChild.pop()
            self.currentChildCount.pop()
            self.leftMost.getToken().depth = len(self.currentChild)
            return self.leftMost
        else:
            # Is finished
            return '' 
        
    def injectType(self, type):
        typeToken = Token('cast', 's>f', self.leftMost.getToken().getLine()) #TODO consider reusing token type of "type"
        typeNode = ParseNode(typeToken)
        typeNode.addChild(self.leftMost) #addChild sets parent
        self.currentNode.setChild(self.currentChild[-1], typeNode)
        
    def getRoot(self):
        return self.root