'''
Created on Jan 25, 2014

@author: mr_hickman

Description:
    Hosts the main function for the compiler, requires an input file for the source code to be compiled. 
    Currently in a state to only tokenize, all most.
'''
from optparse import OptionParser
from scanner import Scanner
import characterCompare

def scan(srcFilePath):
    myScanner = Scanner('TestFiles/test1')
    s = ''
    while True:
        char = myScanner.getNextCharacter()
        s = s + char
        if not char:        #This is the EOF character in python
            print s
            break
    print 'Is Digit:___________________'
    print 'Expected: True,True,False,False,False'
    c =  'Actual: ' + str(characterCompare.isDigit('0')) + ',' + str(characterCompare.isDigit('9')) + ',' + str(characterCompare.isDigit('a'))
    c = c + ',' + str(characterCompare.isDigit('/')) + ',' + str(characterCompare.isDigit(':'))
    print c
    
    print 'Is alpha:___________________'
    print 'Expected: True,True,True,True,False,False,False,False,False'
    c = 'Actual: ' + str(characterCompare.isAlpha('a')) + ',' + str(characterCompare.isAlpha('z')) + ',' + str(characterCompare.isAlpha('Z'))
    c = c + ',' + str(characterCompare.isAlpha('A')) + ',' + str(characterCompare.isAlpha('@')) + ',' + str(characterCompare.isAlpha('['))
    c = c + ',' + str(characterCompare.isAlpha('\'')) + ',' + str(characterCompare.isAlpha('{')) + ',' + str(characterCompare.isAlpha('1'))
    print c
    
    print 'Is Quote:___________________'
    print 'Expected: True,False,False,False'
    c = 'Actual: ' + str(characterCompare.isQuote('"')) + ',' + str(characterCompare.isQuote('\'')) + ',' + str(characterCompare.isQuote('!'))
    c = c + ',' + str(characterCompare.isQuote('#'))
    print c
    
    print 'Is Underscore:___________________'
    print 'Expected: True,False,False,False'
    c = 'Actual: ' + str(characterCompare.isUnderScore('_')) + ',' + str(characterCompare.isUnderScore('-')) + ',' + str(characterCompare.isUnderScore('^')) 
    c = c + ',' + str(characterCompare.isUnderScore('\''))
    print c
    
    print 'Is Keyword:___________________'
    print 'Expected: binop,unop,binop,,'
    c = 'Actual: ' + str(characterCompare.isKeyword('and')) + ',' + str(characterCompare.isKeyword('!')) + ',' + str(characterCompare.isKeyword('^')) 
    c = c + ',' + str(characterCompare.isKeyword('\'')) + ',' + str(characterCompare.isKeyword('ANd'))
    print c
    
    
        
    
    # myLexicalAnalyzer = lexicalAnalyzer(myScanner)
    # myLexicalAnalyzer.tokenize()
    

def main():
    parser = OptionParser("usage: %prog [options] arg1")
    parser.add_option("-s", "--source", dest="SrcFilePath",
                      type="string", default="",
                      help="Input source file path")
    (options, args) = parser.parse_args()
    
    if len(args) != 0:
        parser.error("Incorrect number of arguments provided")
    
    SrcFilePath = options.SrcFilePath
    scan(SrcFilePath)
       
if __name__ == '__main__':
    main()


    