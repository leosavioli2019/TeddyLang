from text import text
from run import start as run
from run import app
from flask import Flask

class console:
    
    def __init__(self):
        self.t = text()
    
    def compile(self, a, terminal=False, port=5000):
        try:
            file = open(a,'r', encoding="utf-8").read()
            file = file.replace("</main>", "")
            run(file, terminal, port)
        except FileNotFoundError:
            print(f"File not Found: {a} does not exists")
        
    def main(self, port=5000):
        self.t.imperative()
        count = 0
        a = ''
        while a != 'exit':
            try:
                a = input('>>>')
            except KeyboardInterrupt:
                print('exit')
                return
            if a.strip() == 'exit' or a.strip() == "exit()":
                break
            self.compile(a, False, port)