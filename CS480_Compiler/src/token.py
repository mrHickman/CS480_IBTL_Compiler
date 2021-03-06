'''
Created on Jan 25, 2014

@author: mr_hickman

Description:
    Class for tokens, which holds the lexems of a descriptive type, value, and currently line number that the 
    token is generated for. 
'''

class Token:
    def __init__(self, tokenType, value, line):
        self.tokenType = tokenType
        self.value = value
        self.line = line
        self.depth = -1
    def printToken(self):
        print '<' + str(self.tokenType) + ', ' + str(self.value) + ', ' + str(self.line) + ', ' + str(self.depth) + '>'
    def getType(self):
        return self.tokenType
    def getLine(self):
        return self.line
    def getValue(self):
        return self.value
    def setValue(self, newValue):
        self.value = newValue