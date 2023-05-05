import interpreter
## shell.py

# just for testing, will overhaul later
while True:
    raw = input('$ ')
    print(interpreter.slang(raw))