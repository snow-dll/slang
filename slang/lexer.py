class LError:
    def __init__(self, message, pos) -> None:
        self.message = message
        self.pos = pos
        self.error = f'\nFatal: Error in Lexer at line {self.pos.ln} \
and column {self.pos.col}: {self.message}\n'

class Position:
    def __init__(self) -> None:
        self.ln = 1
        self.col = 0
        self.idx = -1
    
    def sAdvance(self) -> None:
        self.col += 1
        self.idx += 1

    def nAdvance(self) -> None:
        self.col = 1
        self.ln += 1
        self.idx += 1


## Lexer

class Lexer:
    def __init__(self, inp) -> None:
        self.inp = inp
        self.pos = Position()
        self.cc = None

        # read tokens
        self.tokens = {}
        self.tokensOut = []
        rawStr = ""
        with open('tokens.txt') as tkn_f:
            rawStr = tkn_f.read().split('\n')

        for tkn in rawStr:
            self.tokens[tkn.split(' ')[0]] = tkn.split(' ')[1]
    
    def advance(self) -> None:
        if self.pos.idx >= len(self.inp) - 1:
            # stop
            self.cc = None
            return
        if self.cc == '\n':
            self.pos.nAdvance()
        else:
            self.pos.sAdvance()

        self.cc = self.inp[self.pos.idx]
    
    def lexerNum(self):
        num = ''
        isFloat = False
        while self.cc != None:
            if self.cc not in '0123456789.':
                break
            num += self.cc
            if self.cc == '.':
                isFloat = True
            self.advance()
        if num == '.':
            return 'DOT'
        return ('FLOAT:' if isFloat else 'INT:') + num

    
    def lexerOut(self):
        self.advance()
        isAdv = True
        while self.cc != None:
            if self.cc == '+' or self.cc == '-':
                self.tokensOut.append(self.tokens[self.cc])
                self.tokensOut.append('INT:1')
                self.tokensOut.append('MUL')
            elif self.cc in self.tokens:
                self.tokensOut.append(self.tokens[self.cc])
            elif self.cc == '\n':
                self.tokensOut.append('NEWL')
            elif self.cc in '0123456789.':
                self.tokensOut.append(self.lexerNum())
                isAdv = False
            elif (not self.cc.isalnum()) and self.cc != ' ':
                return [LError('The character is not identifiable.',\
                               self.pos).error, 'e']
            if isAdv:
                self.advance()
            else:
                isAdv = True

        return [self.tokensOut, 'v']