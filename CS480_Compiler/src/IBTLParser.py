'''
Created on Feb 5, 2014

@author: mr_hickman
'''

from token import Token
from lexicalAnalyzer import LexicalAnalyzer
from parseTree import ParseTree
from parseNode import ParseNode
import sys

# TODO add parent logic to each ending

class Parser:
    def __init__(self, lexAnalyzer):
        self.tokenList = lexAnalyzer.tokenList
        if len(self.tokenList) > 1 :
            self.currentToken = self.tokenList[0]
            self.peakToken = self.tokenList[1]
        self.tokenIndx = 1
        self.currentNode = ParseNode(Token('root','root',0))
        self.T()
        self.parseTree = ParseTree(self.currentNode) # Functions pass by value not by reference, important to be after T() call
    
        
        
    def T(self):
        if self.currentToken.value == '[' :
            self.getNextToken()
            if self.currentToken.value != ']' :
                self.S()
                
            # print 'debug assist, token indx = ' + str(self.tokenIndx) + ' length = ' + str(len(self.tokenList))
            
            if self.currentToken.value != ']': 
                self.error()
            if self.tokenIndx + 1 != len(self.tokenList) or self.peakToken:
                self.error()  

        else :
            self.error()
        
    def S(self):
        if self.currentToken.value == '[' :
            self.getNextToken()
            if self.currentToken.value == ']' :
                self.getNextToken()
                self.Sp()
            elif self.currentToken.value == '[' :
                self.getNextToken()
                self.S()
                if self.currentToken.value == ']' :
                    self.getNextToken()
                    self.Sp()
                else :
                    self.error()
            elif self.currentToken.tokenType == 'stmts' :
                self.statement()
                self.Sp()
            elif self.isOperType() :
                self.oper()
                self.Sp()
            elif self.isTerminalType() :
                self.oper()    
                self.Sp()
                if self.currentToken.value != ']':
                    self.error()
                else :
                    self.getNextToken()
                self.Sp()
            else :
                self.error()
        elif self.isTerminalType() :
            self.oper()    
            self.Sp()
        else :
            self.error()
            
    def Sp(self):
        if self.currentToken.value == '[' or self.isTerminalType() :
            self.S()
            self.Sp()
        # the else statement of this is epsilon
        
    def expr(self):
        if self.currentToken.value == '[' :
            self.getNextToken()
            if self.currentToken.tokenType == 'stmts' :
                self.statement()
            elif self.isOperType() :
                self.nonTermOper()
            else :
                self.error()
        elif self.isTerminalType() :
            self.termOper()
        else :
            self.error()
            
    def operExpr(self): #remove when time permits
        if self.currentToken.value == '[' :
            self.getNextToken()
            if self.isOperType() :
                self.nonTermOper()
        elif self.isTerminalType() :
            self.termOper()
        else :
            self.error()
            
    def statement(self):
        if self.currentToken.value == 'if' :
            self.addNonTermNode()
            self.expr()
            self.expr()
            if self.currentToken.value == ']' :
                self.getNextToken()
            else :
                self.expr()
                if self.currentToken.value == ']' :
                    self.getNextToken()
                else :
                    self.error()
        elif self.currentToken.value == 'while' :
            self.addNonTermNode()
            self.expr()
            self.exprlist()
            if self.currentToken.value == ']' :
                self.getNextToken()
            else :
                self.error()
        elif self.currentToken.value == 'let' :
            self.addNonTermNode()
            if self.currentToken.value == '[' :
                self.getNextToken()
                self.varlist()
                if self.currentToken.value == ']' and self.peakToken.value == ']':
                    self.getNextToken()
                    self.getNextToken()
                else :
                    self.error()
            else :
                self.error()
        elif self.currentToken.value == 'stdout' :
            self.addNonTermNode()
            self.oper()
            if self.currentToken.value == ']' :
                self.getNextToken()
            else :
                self.error()
        else:
            self.error()
        self.getParent()
            
    def oper(self):
        if self.isTerminalType() :
            self.termOper()
        else :
            self.nonTermOper()
    
    def termOper(self):
        self.addTermNode()
        
    def nonTermOper(self):
        if self.currentToken.tokenType == 'binop' :
            self.binop()
        elif self.currentToken.tokenType == 'unop' :
            self.unop()
        elif self.currentToken.tokenType == 'op' :
            self.op()
        elif self.currentToken.tokenType == 'assign' :
            self.assign()
        else :
            self.error()
        self.getParent()
            
    def binop(self):
        self.addNonTermNode()
        self.operExpr()
        self.operExpr()
        if self.currentToken.value == ']' :
            self.getNextToken()
        else :
            self.error()
            
    def unop(self):
        self.addNonTermNode()
        self.operExpr()
        if self.currentToken.value == ']' :
            self.getNextToken()
        else :
            self.error()
            
    def op(self):
        self.addNonTermNode()
        self.operExpr()
        if self.currentToken.value == ']' :
            self.getNextToken()
        else :
            self.operExpr()
            if self.currentToken.value == ']' :
                self.getNextToken()
            else :
                self.error()
            
    def assign(self):
        self.addNonTermNode()
        if self.currentToken.tokenType == 'name' :
            self.addTermNode()
            self.operExpr()
            if self.currentToken.value == ']' :
                self.getNextToken()
            else :
                self.error()
        else :
            self.error()
        
    def exprlist(self):
        self.expr()
        if self.currentToken.value != ']' :
            self.exprlist()
    
    def varlist(self):
        if self.currentToken.value == '[' :
            self.getNextToken()
        else :
            self.error()
            
        if self.currentToken.tokenType == 'name' :
            self.addTermNode()
        else :
            self.error()
            
        if self.currentToken.tokenType == 'type' :
            self.addTermNode()
        else :
            self.error()
            
        if self.currentToken.value == ']' :
            self.getNextToken()
        else :
            self.error()
            
        if self.currentToken.value != ']' :
            self.varlist()
        
    def addNonTermNode(self):
        tempNode = ParseNode(self.currentToken)
        self.currentNode.addChild(tempNode)
        self.currentNode = tempNode
        self.getNextToken()
        
    def addTermNode(self):
        self.currentNode.addChild(ParseNode(self.currentToken))
        self.getNextToken()
        
    def getNextToken(self):
        self.currentToken = self.peakToken
        if self.tokenIndx + 1 < len(self.tokenList):
            self.tokenIndx += 1
            self.peakToken = self.tokenList[self.tokenIndx]
        else :
            self.peakToken = ''
        # self.currentToken.printToken()
    def error(self):
            print >> sys.stderr,"Parser error on line " + str(self.currentToken.line) + ' with token value ' + str(self.currentToken.value) + ' token index ' + str(self.tokenIndx)
            sys.stdout.flush()
            raise Exception("Parser error on line " + str(self.currentToken.line) + ' with token value ' + str(self.currentToken.value))
        
    def isTerminalType(self):
        if self.currentToken.tokenType == 'string' or self.currentToken.tokenType == 'int' or self.currentToken.tokenType == 'float' or self.currentToken.tokenType == 'name' :
            return True
        else :
            return False
    
    def getParent(self):
        self.currentNode = self.currentNode.getParent()
        
    def isOperType(self):
        if self.currentToken.tokenType == 'binop' or self.currentToken.tokenType == 'unop' or self.currentToken.tokenType == 'op' or self.currentToken.tokenType == 'assign' :
            return True
        else :
            return False