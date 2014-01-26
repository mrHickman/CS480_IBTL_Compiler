'''
Created on Jan 25, 2014

@author: mr_hickman

Description:
    Facilitates file input massaging for lexical analyzer, by removing comments and duplicate spaces(' ' and '/t').
    Note leaves '/n' characters for line position error reporting. 

'''

'''


'''
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
             
