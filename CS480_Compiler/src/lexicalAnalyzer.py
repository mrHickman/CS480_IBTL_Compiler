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
BUFFERSIZE = 5 # play around with this for optimization
import scanner
import sys
import time 
#checks if token is int or float
class LexicalAnalyzer:
    def digitFSA(self, char):
        num = char
        char = self.getNextChar()
        if not char :
            self.tokenList.append(Token('int', num, self._line))
            return
        
        while characterCompare.isDigit(char):
            num = num + char
            char = self.getNextChar()            
            
        if char != '.': 
            if char == 'e' :
                num = num + char
                char = self.getNextChar()
                if char == '-' :
                    num = num + char
                    char = self.getNextChar()
                    
                while characterCompare.isDigit(char):
                    num = num + char
                    char = self.getNextChar()
                    
                self.tokenList.append(Token('float', num, self._line))
                self.charCheck(char)
                return
            else :
                self.tokenList.append(Token('int', num, self._line))
                self.charCheck(char)
                return
        else:
            self.floatFSA(num)
            # Old float code
            '''num = num + char
            char = self.getNextChar()
            if not char :
                self.tokenList.append(Token('float', num, self._line))
                return
            
            while characterCompare.isDigit(char):
                num = num + char
                char = self.getNextChar()
                
            self.tokenList.append(Token('float', num, self._line))
            self.charCheck(char)
            return'''
        
    def floatFSA(self, char):
        num = char + '.'
        char = self.getNextChar()
        while characterCompare.isDigit(char):
            num = num + char
            char = self.getNextChar()
        
        if char == 'e' :
            num = num + char
            char = self.getNextChar()
            if char == '-' :
                num = num + char
                char = self.getNextChar()
                
            while characterCompare.isDigit(char):
                num = num + char
                char = self.getNextChar()
        else :
            num += 'e'
        
        if num == '.e':
            self.error(num)

        self.tokenList.append(Token('float', num, self._line))
        self.charCheck(char)
        return
            
    def nameFSA(self, char):
        name = char
        char = self.getNextChar()
        if char :
            while characterCompare.isAlpha(char) or characterCompare.isDigit(char) or characterCompare.isUnderScore(char):
                name = name + char
                char = self.getNextChar()
                if not char:
                    break
            
        keyword = characterCompare.isKeyword(name)
        if keyword:
            self.tokenList.append(Token(keyword, name, self._line))
            self.charCheck(char)
        else:
            self.tokenList.append(Token('name', name, self._line))
            self.charCheck(char)
        return
    
    def stringFSA(self, char):
        string = char
        char = self.getNextChar()
        if not char :
            self.error(string)
            return
            
        while characterCompare.isAlpha(char) or characterCompare.isDigit(char):
                string = string + char
                char = self.getNextChar()
            
        if characterCompare.isQuote(char):
            string = string + char
            self.tokenList.append(Token('string', string, self._line))
            char = self.getNextChar()
            self.charCheck(char)
        else:
            self.error(string)
        return
    
    def sepFSA(self, char):
        nextChar = self.getNextChar()
        keyword = characterCompare.isKeyword(char)
        if nextChar :
            twoChar = char + nextChar
            twoKeyword = characterCompare.isKeyword(twoChar)
        else :
            twoKeyword = ''
        if twoKeyword :
            self.tokenList.append(Token(twoKeyword, twoChar, self._line))
            char = self.getNextChar()
            self.charCheck(char)
        elif keyword :
            self.tokenList.append(Token(keyword, char, self._line))
            char = nextChar
            self.charCheck(char)
        else:
            self.error(char)
            char = nextChar
            self.charCheck(char)
        return
    
    def getNextChar(self):
        if self.__bufferPos + 1 < BUFFERSIZE :
            self.__bufferPos += 1
        else : 
            self.fillBuffer()
            
        if self.__currentBuffer == 0:
            char = self.__buffer0[self.__bufferPos]
        else : 
            char = self.__buffer1[self.__bufferPos]

        if char == '' :
            self.__isEof = True     
            
        return char
        
    def fillBuffer(self):
        self.__bufferPos = 0
        if self.__currentBuffer == 0 :
            self.__currentBuffer = 1
            for x in range(0, BUFFERSIZE):
                self.__buffer1[x] = self.__myScanner.getNextCharacter()
        else :
            self.__currentBuffer = 0
            for x in range(0, BUFFERSIZE):
                self.__buffer0[x] = self.__myScanner.getNextCharacter()
           
    def error(self, string):
        print >> sys.stderr, "Error on line " + str(self._line) + ": " + string + " is not valid"
    
    def charCheck(self, currentChar):
        if self.__isEof :
            return
        
        if currentChar == ' ' :
            currentChar = self.getNextChar()
            
        if currentChar == '\n' :
            self._line += 1
            currentChar = self.getNextChar()
            self.charCheck(currentChar)
            return
        
        if characterCompare.isDigit(currentChar):
            self.digitFSA(currentChar)
        elif currentChar == '.':
            self.floatFSA('')
        elif characterCompare.isAlpha(currentChar) or characterCompare.isUnderScore(currentChar):
            self.nameFSA(currentChar)
        elif characterCompare.isQuote(currentChar):
            self.stringFSA(currentChar)
        else:
            self.sepFSA(currentChar)
        return
    
    def __init__(self, myFile):
        self.tokenList = []
        self._line = 1    #current line number
        self.__currentBuffer = 0
        self.__buffer0 = ['']*BUFFERSIZE
        self.__buffer1 = ['']*BUFFERSIZE
        self.__isEof = False
        self.__myScanner = scanner.Scanner(myFile)
        self.fillBuffer()
        self.__bufferPos = -1
        self.charCheck(self.getNextChar())  