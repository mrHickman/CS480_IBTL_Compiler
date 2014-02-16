'''
Created on Feb 5, 2014

@author: mr_hickman
'''
class ParseNode:
    def __init__(self, token):
        self._parent = '' # if left unchanged then '' is a root node
        self.token = token
        self.children = []
        
    def getToken(self):
        return self.token
    
    def getParent(self):
        return self._parent
    
    def addChild(self, childParseNode):
        childParseNode._parent = self
        self.children.append(childParseNode)
            
    def getChildCount(self):
        return len(self.children)
    
    def getChild(self, indx):
        if indx < len(self.children) : # this is redundant in this implementation
            return self.children[indx]
        else :
            return ''
        