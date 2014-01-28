'''
Created on Jan 25, 2014

@author: mr_hickman

Description:
    This is the primary tokenizing class. Using scanner to clean up the input from the file it 
    traverses our dfa model to determine what attributes a token requires and produces the tokens.
'''
from constants.py import BUFFERSIZE as BUFFERSIZE


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
