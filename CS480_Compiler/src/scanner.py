'''
Created on Jan 25, 2014

@author: mr_hickman

Description:
    Facilitates file input massaging for lexical analyzer, by removing comments(//,/*/, and /*...*/) and 
    duplicate spaces(' ' and '\t'). Notes: leaves '/n' characters for line position error reporting, and 
    converts '\t' to ' '. 

'''
class Scanner:
    def __init__(self, srcFilePath):
        self.srcFilePath = srcFilePath
        self.file = open(self.srcFilePath, 'r')
        self.isMultiLineComment = False
        self.current = ''
        self.peak = self.file.read(1)
        self.last = ''
                
    def _readNextCharacter(self):
        self.current = self.peak
        self.peak = self.file.read(1)
        return
        
    def getNextCharacter(self):
        
        self._readNextCharacter()
        
        if self.current == '\t' :
            self.current = ' '
            
        if (self.last == ' ' or self.last == '\n') and self.current == ' ':
            while self.peak == ' ' or self.peak == '\t' :
                self.peak = self.file.read(1)
            self.getNextCharacter()
            
        if self.current == '/' and self.peak == '/' :
            while self.current != '\n' and self.current:
                self._readNextCharacter()
                
        if self.current == '/' and self.peak == '*' :
            self.isMultiLineComment = True
                                    
        while self.isMultiLineComment and self.current != '\n' and self.current:
            self._readNextCharacter()
            if self.current == '*' and self.peak == '/' : 
                self.isMultiLineComment = False
                self._readNextCharacter()
                self.getNextCharacter() # Case for /**//**/
            
        self.last = self.current        
        return self.current       
