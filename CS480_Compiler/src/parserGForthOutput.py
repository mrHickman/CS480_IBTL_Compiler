'''
Created on Feb 27, 2014

@author: mr_hickman
'''

class ParserGForthOutput:
    '''
    classdocs
    '''
    
    def __init__(self, parseTree):

        self.parseTree = parseTree
        self.currentNode = ''
        self.peakNode = self.parseTree.getNextLeftMostNode()
        self.getNextNode()
        self.gForth = ''
        self.generateGForth()
        
    
    def getNextNode(self):
        self.currentNode =  self.peakNode
        self.peakNode = self.parseTree.getNextLeftMostNode()
    
    def generateGForth(self):
        while self.peakNode:
            self.gForth += self.currentNode.getValue() + ' '
            self.getNextNode()
        print self.gForth