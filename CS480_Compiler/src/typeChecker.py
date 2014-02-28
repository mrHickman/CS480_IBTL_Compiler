from parseTree import ParseTree
from operationType import OperationType
import sys
class TypeChecker:
    def __init__(self, parseTree):
        self.ParseTree = parseTree
        self.currentNode = ''
        self.childCountStack = []
        self.typeStack = []
        self.getNextNode()
        self.checkType()
        
    def checkType(self):
        while self.currentNode.getParent() : # current will be the root at fail
            while self.isTypeTerminal() and self.currentNode.getParent() :
                self.getNextNode()
                
            if not self.currentNode.getParent() :
                return #At Root Node
            
            paramList = self.checkParamSets()
            
#             print 'typeStack:'
#             print self.typeStack #Debug Print
#             print 'paramList: ' 
#             print paramList #Debug Print

            if not paramList :
                self.error()
            else :
                self.pop(paramList[-1])
            
        # Catch IF WHILE LET ?
    def error(self):
        print >> sys.stderr,"Semantic error on line " + str(self.currentNode.getToken().getLine()) + ' with token value ' + str(self.currentNode.getToken().getValue())
        sys.stdout.flush()
        raise Exception("Semantic error on line " + str(self.currentNode.getToken().getLine()) + ' with token value ' + str(self.currentNode.getToken().getValue()))
        
    def checkParamSets(self):
        possParam = OperationType[self.currentNode.getToken().getValue()]
        for x in range(0, len(possParam)) :
            if len(possParam[x]) == self.childCountStack[-1] + 1:
                for y in range(0, len(possParam[x])-1):
                    if self.typeStack[-y-2] == possParam[x][y]:
                        isValid = True
                    else :
                        isValid = False
                        break
                if isValid:
                    return possParam[x]
                
        for z in range(0, self.childCountStack[-1]):
            if self.typeStack[-z-2] == 'int':
                self.convertScopeToFloat()
                return self.checkParamSets()
        return ''
            
        
    def isTypeTerminal(self):
        tempType = self.typeStack[-1]  
        if tempType == 'bool' or tempType == 'int' or  tempType == 'float' or tempType == 'string' or tempType == 'name':
            return True
        else :
            return False
        
    def getNextNode(self):
        self.currentNode = self.ParseTree.getNextLeftMostNode()
        self.childCountStack.append(self.currentNode.getChildCount())
        self.typeStack.append(self.currentNode.getToken().getType())
    
    def pop(self, returnType):
        argumentCount = self.childCountStack[-1]
        for x in range(0, argumentCount + 1) :
            self.childCountStack.pop()
            self.typeStack.pop()
        
        if returnType :
            self.typeStack.append(returnType)
            self.childCountStack.append(0)
        
    def getScopeNode(self):
        currentScopeNode = self.currentNode
        parentNode = currentScopeNode.getParent()
        while self.isNumOper(parentNode):
            currentScopeNode = parentNode
            parentNode = currentScopeNode.getParent()
        return currentScopeNode
    
    def convertScopeToFloat(self):
        tempTree = ParseTree(self.getScopeNode())
        currentNode = tempTree.getNextLeftMostNode()
        while currentNode != tempTree.getRoot():
            if currentNode.getToken().getType() == 'int':
                tempTree.injectType('float')            
            currentNode = tempTree.getNextLeftMostNode()
        
        for x in range (0, len(self.typeStack)) :
            if self.typeStack[x] == 'int':
                self.typeStack[x]  = 'float'
                
    def isNumOper(self, node):
        value = node.getToken().getValue()
        numOps = ['+', '-', '*', '^', '%', '/', '=', '<', '>', '<=', '>=', '!=', 'not_eq', 'sin', 'cos', 'tan', '++', '--', '-', 'if']
        try : 
            numOps.index(value)
            return True
        except :
            return False