import slang.interpreter
## shell.py

# just for testing, will overhaul later
while True:
    raw = input('$ ')
    print(slang.interpreter.slang(raw))