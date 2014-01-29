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
                
    def readNextCharacter(self):
        self.current = self.peak
        self.peak = self.file.read(1)
        return
        
    def getNextCharacter(self):
        
        self.readNextCharacter()
        
        if self.current == '/' and self.peak == '/' :
            while self.current != '\n' and self.current:
                self.readNextCharacter()
                
        if self.current == '/' and self.peak == '*' :
            self.isMultiLineComment = True
            self.readNextCharacter()
                                    
        while self.isMultiLineComment and self.current != '\n' and self.current:
            self.readNextCharacter()
            if self.current == '*' and self.peak == '/' : 
                self.isMultiLineComment = False
                self.readNextCharacter()
                self.getNextCharacter() # Case for /**//**/
                
        if (self.current == ' ' or self.current == '\t') and (self.peak == ' ' or self.peak == '\t') :
            self.current = ' '
            while self.peak == ' ' or self.peak == '\t' :
                self.peak = self.file.read(1)
                
        return self.current
             
