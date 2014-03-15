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
        
        print self.gForth
        
    
    def getNextNode(self):
        self.currentNode =  self.peakNode
        self.peakNode = self.parseTree.getNextLeftMostNode()
    
    def generateGForth(self):
        myRoot = self.parseTree.getRoot()
        children = myRoot.children
        letTrees = []
        for x in range(0, len(children)):
            if myRoot.getChild(x).getValue() == 'let' :
                letTrees.append(x)
        if len(letTrees) > 0 and letTrees[0] == 0 :
            self.printLets() #add the variable assignments here
        self.gForth += ': prgm '
        while self.peakNode:
            if len(letTrees) > 0 and self.parseTree.currentChild[0] in letTrees and self.currentNode.getType() == 'name': # is in letTrees
                self.gForth += '; \n prgm \n'
                self.printLets()
                self.gForth += ': prgm '
                if self.peakNode and self.parseTree.currentChild[0] in letTrees and self.currentNode.getType() == 'name':
                    continue
                elif not self.peakNode :
                    break
            self.gForth += self.currentNode.getValue() + ' '
            self.getNextNode()
        self.gForth += '; \n prgm \n' # may need to switch to \r

    def printLets(self):
        self.gForth += '\n'
        while True :
            if self.currentNode.getType() == 'name':
                tempString = ''
                tempString += self.currentNode.getValue() + ' '
                self.getNextNode()
                if self.currentNode.getValue() == 'int' or self.currentNode.getValue() == 'bool' :
                    self.gForth += 'variable ' + tempString
                elif self.currentNode.getValue() == 'float' :
                    self.gForth += 'fvariable ' + tempString
                elif self.currentNode.getValue() == 'string' :
                    self.gForth += 'create ' + tempString + '1024 chars allot '
                else: 
                    self.error()
                    break
                self.getNextNode()
            else:
                self.gForth += '\n'
                self.getNextNode()
                break
        
            
    def error(self):
        print 'ERRROR'
                    
        
        