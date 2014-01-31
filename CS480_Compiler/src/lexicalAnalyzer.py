'''
Created on Jan 25, 2014

@author: mr_hickman

Description:
    This is the primary tokenizing class. Using scanner to clean up the input from the file it 
    traverses our dfa model to determine what attributes a token requires and produces the tokens.
'''

'''
regular expression for each of the 
strings     = ^"[a-zA-Z0-9]*"$ # We moved True and False to keywords 
name        = ^[a-zA-Z_][a-zA-Z0-9_]*$
ints        = ^[0-9][0-9]*$
floats      = ^[0-9][0-9]*.[0-9]*$|^[0-9][0-9]*e[0-9][0-9]*$
keyword     = Check via symbol table and label appropriately
                ex. <comparison, <>
                    <stmts, if>
other       = ()|[]|{}|,|;|:|eof


keywords currently in symbol table
++|--|?|!|not|+|-|*|/|%|^|or|'||'|and|'&&'|if|while|
let|stdout|&|->|=|<|<=|=<|>|>=|=>|==|!=|not_eq|true|false

+|-|*|/|%|^|or|'||'|and|'&&'|if|while|
let|stdout|=

''' 

from token import Token
import characterCompare
from constants import BUFFERSIZE as BUFFERSIZE
import scanner

#checks if token is int or float
def digitFSA(self, char):
    num = char
    while characterCompare.isDigit(char):
        num = num + char
        char = getNextChar()            
        
    if char != '.':
        self.tokenList.append(Token('int', num, self._line))
        
        charCheck(char)
        return
    else:
        num = num + char
        char = getNextChar()
        while characterCompare.isDigit(char):
            num = num + char
            char = getNextChar()
        self.tokenList.append(Token('float', num, self._line))
    charCheck(char)
    return

def nameFSA(self, char):
    name = char
    char = getNextChar()
    while characterCompare.isAlpha(char) or characterCompare.isDigit(char) or characterCompare.isUnderScore(char):
        name = name + char
        char = getNextChar()
    keyword = characterCompare.isKeyword(name)
    if keyword:
        self.tokenList.append(Token(keyword, name, self._line))
        
        charCheck(char)
    else:
        self.tokenList.append(Token('name', name, self._line))
        
        charCheck(char)
    return

def stringFSA(self, char):
    string = char
    char = getNextChar()
    while characterCompare.isAlpha(char) or characterCompare.isDigit(char):
        string = string + char
        char = getNextChar()
        
    if characterCompare.isQuote(char):
        string = str + char
        self.tokenList.append(Token('string', str, self._line))
        
        char = getNextChar()
        charCheck(char)
    else:
        error(string)
    return

def sepFSA(self, char):
    nextChar = getNextChar()
    twoChar = char + nextChar
    twoKeyword = characterCompare.isKeyword(twoChar)
    keyword = characterCompare.isKeyword(char)
    if twoKeyword:
        self.tokenList.append(Token(twoKeyword, twoChar, self._line))
        char = getNextChar()
        charCheck(char)
    elif keyword:
        self.tokenList.append(Token(keyword, char, self._line))
        char = nextChar
        charCheck(char)
    else:
        error(char)
        char = getNextChar()
        charCheck(char)
    return

def getNextChar(self):
    if self.__bufferPos < BUFFERSIZE :
        self.__bufferPos += 1
    else : 
        fillBuffer()
        
    if self.__currentBuffer :
        char = self.__buffer1[self.__bufferPos]
    else : 
        char = self.__buffer0[self.__bufferPos]
        
    if char == '\n':                    #checks for end of line character
            self._line += 1
            char = getNextChar()
            
    return char
    
def fillBuffer(self):
    self.__bufferPos = 0
    self.__currentBuffer = not self.__currentBuffer
    if self.__currentBuffer :
        for x in range(0, BUFFERSIZE):
            self.__buffer1[x] = self.__myScanner.getNextChar()
    else :
        for x in range(0, BUFFERSIZE):
            self.__buffer0[x] = self.__myScanner.getNextChar()
       
#     while True LOGIC:
#         char = __myScanner.getNextCharacter()
#         if not char:        #This is the EOF character in python
#             break
    #gets the next character from buffer
    #checks if buffer is empty
    #if buffer is empty then it fills it and switches to other buffer
    #returns the next character
    #edits the global variables buffer and pos

def error(self, string):
    print "Error on line " + self._line + ": " + string + " is not valid\n"

def charCheck(currentChar):
    if currentChar == '' :
        return
    if characterCompare.isDigit(currentChar):
        digitFSA(currentChar)
    elif characterCompare.isAlpha(currentChar) or characterCompare.isUnderScore(currentChar):
        nameFSA(currentChar)
    elif characterCompare.isQuote(currentChar):
        stringFSA(currentChar)
    else:
        sepFSA(currentChar)
    return

def __init__(self, myFile):
    self.tokenList = []
    self._line = 1    #current line number
    self.__bufferPos = 0
    self.__currentBuffer = 0
    self.__buffer0 = ['']*BUFFERSIZE
    self.__buffer1 = ['']*BUFFERSIZE
    self.__myScanner = scanner.Scanner(myFile)
    charCheck(getNextChar())
    
    
    
        
