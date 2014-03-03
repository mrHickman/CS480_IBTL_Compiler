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
        self.gForth = ': prgm '
        self.generateGForth()
        self.gForth += '; \n prgm \n bye' # may need to switch to \r
        print self.gForth
        
    
    def getNextNode(self):
        self.currentNode =  self.peakNode
        self.peakNode = self.parseTree.getNextLeftMostNode()
    
    def generateGForth(self):
        while self.peakNode:
            self.gForth += self.currentNode.getValue() + ' '
            self.getNextNode()
