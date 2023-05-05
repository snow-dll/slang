import lparser
## Interpreter

class Interpreter:
    def __init__(self, inp) -> None:
        self.inp = lparser.LParser(inp).lparserOut()[0]
        self.flag = lparser.LParser(inp).lparserOut()[1]
    
    def interpreterOut(self):
        #to be modified
        if self.flag == 'e':
            return self.inp
        return self.inp


## def slang

def slang(inp):
    return Interpreter(inp).interpreterOut()