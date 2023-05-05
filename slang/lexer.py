# read tokens
tokens = {}
raw_str = ""
with open('tokens.txt') as tkn_f:
    raw_str = tkn_f.read().split('\n')

for tkn in raw_str:
    tokens[tkn.split(' ')[0]] = tkn.split(' ')[1]


class Position:
    def __init__(self) -> None:
        self.ln = 1
        self.col = 1
        self.idx = 0
    
    def s_advance(self) -> None:
        self.col += 1
        self.idx += 1

    def n_advance(self) -> None:
        self.col = 1
        self.ln += 1
        self.idx += 1 


## Lexer

class Lexer:
    def __init__(self, inp) -> None:
        self.inp = inp
        self.pos = Position()
        self.cc = None
    
    def advance(self) -> None:
        if self.pos.idx >= len(self.inp) - 1:
            # stop
            self.cc = None
            return 0
        if self.cc == '\n':
            self.pos.n_advance()
        else:
            self.pos.s_advance()

        self.cc = self.inp[self.pos.idx]
    
    def lexerOut(self):
        #to be modified
        return self.inp