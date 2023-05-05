import lparser
## Interpreter

class Interpreter:
    def __init__(self, inp) -> None:
        self.inp = lparser.LParser(inp).lparserOut()
    
    def interpreterOut(self):
        #to be modified
        return self.inp


## def slang

def slang(inp):
    return Interpreter(inp).interpreterOut()