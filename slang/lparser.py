import lexer

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
        
        if 'NEWL' in self.inp:
            outputs = []
            lines = self.inp.split('NEWL')
        else:
            lines = [self.inp]
    
    def parserForth(self, lines):
        linecount = 0
        for line in lines:
            linecount += 1
            pass


        return [self.inp, self.flag]