'''
Created on Jan 29, 2014

@author: mr_hickman

Description: Used as helper functions for the dfa in the lexicalAnalyzer.py
'''
from symbolTable import SymbolTable as symbolTab

def isDigit(char):
    var = ord(char)
    if var <= 57 and var >= 48 :
        return True
    else :
        return False

def isAlpha(char):
    var = ord(char)
    if (var <= 90 and var >= 65) or (var <= 122 and var >= 97) :
        return True
    else :
        return False

def isKeyword(s):
    if s in symbolTab.keys():
        return symbolTab[s]
    else:
        return ''

def isQuote(char):
    if char == '"' :
        return True
    else :
        return False
    
def isUnderScore(char):
    if char == '_' :
        return True
    else :
        return False