import os

def lichess():
    program = "python3"
    arguments = ["lishogi-bot.py","-u"]
    print(os.execvp(program, (program,) +  tuple(arguments)))
lishogi()
