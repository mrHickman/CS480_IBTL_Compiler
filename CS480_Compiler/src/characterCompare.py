'''
Created on Jan 29, 2014

@author: mr_hickman

Description: Used as helper functions for the dfa in the lexicalAnalyzer.py
'''
from symbolTable import symbolTable as symbolTab

def isDigit(char):
    char = ord(char)
    if char <= 57 and char >= 48 :
        return True
    else :
        return False

def isAlpha(char):
    char = ord(char)
    if (char <= 90 and char >= 65) or (char <= 122 and char >= 97) :
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