'''
Created on Feb 5, 2014

@author: mr_hickman
'''
class ParseNode:
    def __init__(self, token):
        self.token = token,
        self.children = []
        
    def getChildren(self):
        return self.children
    
    def getToken(self):
        return self.token
    
    def addChild(self, childParseNode):
        self.children.append(childParseNode)
    
    # removeChild ?
    
        