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
    def printToken(self):
        print '<'+str(self.tokenType)+', '+ str(self.value) +', '+ str(self.line) +'>'