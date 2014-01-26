'''
Created on Jan 25, 2014

@author: mr_hickman

Description:
    Hosts the main function for the compiler, requires an input file for the source code to be compiled. 
    Currently in a state to only tokenize, all most.
'''
from optparse import OptionParser
from scanner import Scanner

def scan(srcFilePath):
    myScanner = Scanner('TestFiles/test1')
    while True:
        char = myScanner.getNextCharacter()
        if not char:        #This is the EOF character in python
            break
        else:
            print char
    
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


    