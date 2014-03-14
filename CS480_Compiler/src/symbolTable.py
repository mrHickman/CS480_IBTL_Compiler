'''
Created on Jan 28, 2014

@author: anton_000

Description: 
    Symbol Table to hold the keywords and identifiers for reference
'''

SymbolTable = {'and'    :   'binop',
               'or'     :   'binop',
               '*'      :   'binop',
               '/'      :   'binop',
               '%'      :   'binop',
               '^'      :   'binop',
               '||'     :   'binop',
               '&&'     :   'binop',
               '+'      :   'binop',
               '='      :   'binop',
               '<'      :   'binop',
               '>'      :   'binop',
               '<='     :   'binop',
               '>='     :   'binop',
               '!='     :   'binop',
               'not_eq' :   'binop',
               
               'not'    :   'unop',
               'sin'    :   'unop',
               'cos'    :   'unop',
               'tan'    :   'unop',
               '++'     :   'unop',
               '--'     :   'unop',
               '!'      :   'unop',
               
               '-'      :   'op',

               'if'     :   'stmts',
               'while'  :   'stmts',
               'let'    :   'stmts',
               'stdout' :   'stmts',
               
               '['      :   'paren',
               ']'      :   'paren',
                              
               ':='     :   'assign',
               
               'bool'   :   'type',
               'int'    :   'type',
               'float'  :   'type',
               'string' :   'type',
               
               'true'   :   'bool',
               'false'  :   'bool',
               
               's>f' : 'cast'
               }
VariableTable = {}