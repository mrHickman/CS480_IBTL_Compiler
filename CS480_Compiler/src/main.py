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
from lexicalAnalyzer import LexicalAnalyzer

def scan(srcFilePath):
    myScanner = Scanner(srcFilePath)
    s = ''
    while True:
        char = myScanner.getNextCharacter()
        s = s + char
        if not char:        #This is the EOF character in python
            print s
            break
        
def testCharacterCompare():
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
    
def lexicalAnalyzer(myFile):
    myLexicalAnalyzer = LexicalAnalyzer(myFile)
    for x in myLexicalAnalyzer.tokenList:
        x.printToken()
    # myLexicalAnalyzer.tokenize()
    

def main():
    parser = OptionParser("usage: %prog [options] arg1")
    parser.add_option("-s", "--source", dest="SrcFilePath",
                      type="string", default='',
                      help="Input source file path")
    parser.add_option("-d", "--debug", dest="DebugMode",
                      type="string", default='',
                      help="Debug Mode y:''")
    (options, args) = parser.parse_args()
    
    if not len(args) <= 1:
        parser.error("Incorrect number of arguments provided")
    
    if options.DebugMode :
        scan(options.SrcFilePath)
        testCharacterCompare()
    lexicalAnalyzer(options.SrcFilePath)
    
if __name__ == '__main__':
    main()


    