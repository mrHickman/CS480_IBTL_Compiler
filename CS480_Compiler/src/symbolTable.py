'''
Created on Jan 28, 2014

@author: anton_000

Description: 
    Symbol Table to hold the keywords and identifiers for reference
'''

symbolTable = {'and'    :   'binop',
               'or'     :   'binop',
               '*'      :   'binop',
               '/'      :   'binop',
               '%'      :   'binop',
               '^'      :   'binop',
               '||'     :   'binop',
               '&&'     :   'binop',
               '+'      :   'binop',
               '='      :   'binop',
               
               'not'    :   'unop',
               'sin'    :   'unop',
               'cos'    :   'unop',
               'tan'    :   'unop',
               '++'     :   'unop',
               '--'     :   'unop',
               '!'      :   'unop',
               
               '-'      :   'op',

               '?'      :   'terop',
               
               '=='     :   'relop',
               '<'      :   'relop',
               '>'      :   'relop',
               '<='     :   'relop',
               '>='     :   'relop',
               '!='     :   'relop',
               'not_eq' :   'relop',
               
               'if'     :   'state',
               'while'  :   'state',
               'let'    :   'state',
               'stdout' :   'state',
               
               '('      :   'paren',
               ')'      :   'paren',
               '['      :   'paren',
               ']'      :   'paren',
               '{'      :   'paren',
               '}'      :   'paren',
               
               ','      :   'sep',
               ';'      :   'sep',
               ':'      :   'sep',
               ''       :   'sep' # EOF
               }