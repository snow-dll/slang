import lexer

class PError:
    def __init__(self, message, ln) -> None:
        self.message = message
        self.ln = ln
        self.error = f'\nFatal: Error in Parser at line {self.pos.ln}\
: {self.message}\n'

class LangTree:
    def __init__(self, head) -> None:
        self.head = head
    
    def __repr__(self) -> str:
        return f'{self.head}'

class OpNode:
    def __init__(self, selfVal, leftChild, rightChild) -> None:
        self.selfVal = selfVal
        self.leftChild = leftChild
        self.rightChild = rightChild
    
    def __repr__(self) -> str:
        return f'{self.selfVal} < {self.leftChild.selfVal}, \
{self.rightChild.selfVal}'


## LParser

class LParser:
    def __init__(self, inp) -> None:
        self.inp = lexer.Lexer(inp).lexerOut()[0]
        self.flag = lexer.Lexer(inp).lexerOut()[1]
    
    def lparserOut(self):
        #to be modified
        if self.flag == 'e':
            return [self.inp, self.flag]
        
        # if 'NEWL' in self.inp:
        #     outputs = []
        #     lines = self.inp.split('NEWL')
        # else:
        #     lines = [self.inp]
        return [self.inp, self.flag]
    
    def parserForth(self, lines):
        # lineCount = 0
        # for line in lines:
        #     parCount = 0
        #     lineCount += 1

        #     currentNode = None
        #     while True:
        #         if len(line) == 1:
        #             break
        #         if line[1] == 'LPAR' and line[-1] == 'RPAR':
        #             line = line[1:-1]
        #         didSplit = False
        #         for tkn in line:
        #             if tkn == 'LPAR': parCount += 1
        #             if tkn == 'RPAR': parCount -= 1
        #             if (tkn == 'PLS' or tkn == 'MIN') and parCount == 0:
        #                 didSplit = True


                        
            


        return [self.inp, self.flag]