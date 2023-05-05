import lexer
## LParser

class LParser:
    def __init__(self, inp) -> None:
        self.inp = lexer.Lexer(inp).lexerOut()
    
    def lparserOut(self):
        #to be modified
        return self.inp