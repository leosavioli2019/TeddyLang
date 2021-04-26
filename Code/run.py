from teddymark.teddymark import ex as exe
import ex
import keywords
from flask import Flask

page = ''
terminal = False
app = Flask(__name__)

def PRINT(string):
    global page
    if not terminal:
        page += str(string)
    else:
        print(string)
    
def TPRINT(string):
    global page
    if not terminal:
        page += exe(str(string))
    else:
        print(string)

@app.route('/')
def MainRoute():
    return page

def run(string, terminals=False):
    global page
    global terminal
    terminal = terminals
    a = ex.Inter(string, keywords.keywords,keywords.pythonEqual)
    if a.result == None:
        for c in range(0, len(a.tm)):
            page += exe(a.tm[c])
            cod = ''
            try:
                cod = a.tl[c]
            except IndexError:
                pass
            exec(cod)
        if not terminal:
            app.run()        
    else:    
        print(a.result)