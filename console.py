from text import text
from run import *

class console:
    
    def __init__(self):
        self.t = text()
    
    def compile(self, a, terminal=False):
        try:
            file = open(a,'r', encoding="utf-8").read()
            file = file.replace("</main>", "")
            run(file, terminal)
        except FileNotFoundError:
            print(f"File not Found: {a} does not exists")
        
    def main(self):
        self.t.imperative()
        a = ''
        while a != 'exit':
            a = input('>>>')
            if a.strip() == 'exit' or a.strip() == "exit()":
                break
            self.compile(a)