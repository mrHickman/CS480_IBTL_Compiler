'''
Created on Jan 25, 2014

@author: mr_hickman

Description:
    Facilitates file input massaging for lexical analyzer, by removing comments and duplicate spaces(' ' and '/t').
    Notes: leaves '/n' characters for line position error reporting, and converts '/t' to ' '. 

'''

'''


'''
from constants import BUFFERSIZE as BUFFERSIZE

class Scanner:
    def __init__(self, srcFilePath):
        self.srcFilePath = srcFilePath
        self.currentBufferPos = BUFFERSIZE
        self.currentFilePos = 0;
        self.buffer = [''] * BUFFERSIZE
        self.file = open(self.srcFilePath, 'r')
                
    def __fillBuffer(self):
        for i in range(0, BUFFERSIZE):
            self.buffer[i] = self.file.read(1)
            if not self.buffer[i]:
                break
            
    def __getNextPos(self):
        self.currentBufferPos += 1
        if self.currentBufferPos >= BUFFERSIZE:
            self.currentBufferPos = 0
            self.__fillBuffer()
             
    def getNextCharacter(self):
        self.__getNextPos()
        # add all the checking here
        # ord(char) gives ascii int value
        return self.buffer[self.currentBufferPos]

# File
# ReadBuffer
# CurrentPos
# BufferSize == BUFFER_SIZE


# get next character{
    # If(ReadBuffer[currentpos] == '//')
        # While(next ! /n)
            # skip
        # return /n
    # If(IsMultiLineComment || (ReadBuffer[currentpos] == / && ReadBuffer[currentpos++] == *))
        # While(next ! /n || (* && next /))
            # skip
        # If (* && next /)
            # IsMultiLineComment = false
            # skip through the */
            # return next
        # IsMultiLineComment = true
        # return /n
    # If(ReadBuffer[currentpos] == ' ' || /t )    
        # While(next ' ' || '/t')
            # skip, ++CurrentPos; # if at the end of a buffer then skip will remain in this loop for white space prior
        # return ' '
    # return ReadBuffer[CurrentPos++] # look for eof up one level
# skip
        # if(CurrentPos++ < BufferSize)
                # return;
        # else 
            # fill buffer and set currentPos = 0
# fill buffer
             