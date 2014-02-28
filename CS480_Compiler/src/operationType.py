'''
Created on Jan 28, 2014

@author: anton_000

Description: 
    Symbol Table to hold the keywords and identifiers for reference
'''
# Values are determined via, 0-n-2 are argument param, n-1 is return type
OperationType = {'and'    :  [['bool', 'bool', 'bool']],
               'or'     :   [['bool', 'bool', 'bool']],
               '||'     :   [['bool', 'bool', 'bool']],
               '&&'     :   [['bool', 'bool', 'bool']],
               '!'      :   [['bool', 'bool']],
               'not'    :   [['bool', 'bool']],

               '*'      :   [['int', 'int', 'int'], ['float', 'float', 'float']],
               '/'      :   [['int', 'int', 'int'], ['float', 'float', 'float']],
               '%'      :   [['int', 'int', 'int'], ['float', 'float', 'float']],
               '^'      :   [['float', 'float', 'float']],
               '+'      :   [['int', 'int', 'int'], ['float', 'float', 'float'], ['string', 'string', 'string']],               
               
               '='      :   [['int', 'int', 'bool'], ['float', 'float', 'bool']],
               '<'      :   [['int', 'int', 'bool'], ['float', 'float', 'bool']],
               '>'      :   [['int', 'int', 'bool'], ['float', 'float', 'bool']],
               '<='     :   [['int', 'int', 'bool'], ['float', 'float', 'bool']],
               '>='     :   [['int', 'int', 'bool'], ['float', 'float', 'bool']],
               '!='     :   [['int', 'int', 'bool'], ['float', 'float', 'bool']],
               'not_eq' :   [['int', 'int', 'bool'], ['float', 'float', 'bool']],
               
               'sin'    :   [['float', 'float']],
               'cos'    :   [['float', 'float']],
               'tan'    :   [['float', 'float']],
               
               '++'     :   [['int', 'int'], ['float', 'float']],
               '--'     :   [['int', 'int'], ['float', 'float']],
               
               
               '-'      :   [['int', 'int'], ['float', 'float'], ['int', 'int', 'int'], ['float', 'float', 'float']],

               'if'     :   [['bool', 'int', 'int'], ['bool', 'float', 'float'], ['bool', 'string', 'string'], 
                             ['bool', 'bool', 'bool'], ['bool', '', ''], 
                             ['bool', 'int', 'int', 'int'], ['bool', 'float', 'float', 'float'], ['bool', 'string', 'string', 'string'], 
                             ['bool', 'bool', 'bool', 'bool'], ['bool', '', '', '']
                            ],
                 
               'stdout' :   [['string'], ''],
                              
               ':='     :   [['name', 'bool', ''], ['name', 'int', ''], ['name', 'float', ''], ['name', 'string', '']],
               
               's>f' : [['int', 'float'], ['float', 'float']],
               
               'while'  :   [['?']], #These are unique and require additional logic to type check
               'let'    :   [['?']]
               }