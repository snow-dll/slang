import lexer
## LParser

class LParser:
    def __init__(self, inp) -> None:
        self.inp = lexer.Lexer(inp).lexerOut()[0]
        self.flag = lexer.Lexer(inp).lexerOut()[1]
    
    def lparserOut(self):
        #to be modified
        if self.flag == 'e':
            return [self.inp, self.flag]
        return [self.inp, self.flag]