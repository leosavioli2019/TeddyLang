from teddymark.teddymark import ex as exe
import ex
import keywords
import getUrls
import util
from flask import Flask, request
from errors import Error
from remove import RemoveTag
from optimaze import Optimaze

page : str = ''
terminal : bool = False
app = Flask(__name__)
count : int = 0

def PRINT(v : str, string : str) -> str:
    result : str = v
    if not terminal:
        result += string
    else:
        print(string)
    return result
    
def TPRINT(v : str, string : str) -> str:
    result : str = v
    if not terminal:
        result += exe(string)
    else:
        print(string)
    return result

class run:
    
    def __init__(self, terminal : bool = False, new = None, method=None):
        self.result : str = ''
        self.terminal : bool = terminal
        self.new = new
        self.req = method
        self.main()
    
    def addT(self, string : str) -> None:
        self.result = TPRINT(self.result, string)
        return
        
    def addP(self, string : str) -> None:
        self.result = PRINT(self.result, string)
        return

    def getGlobal(self,var):
        return eval(var)
    
    def setGlobal(self, var, value, isClass='') -> None:
        if isClass == '':
            if type(var) == str:
                exec(f"""global {var}\n{var} = '{value}'""")
            else:
                exec(f"""global {var}\n{var} = {value}""")
        elif isClass == 'class':
            class clone(value):
                pass
            exec(f"""global {var}\n{var} = clone""")
        elif isClass == 'function':
            exec(f"""global {var}\n{var} =""")
        else:
            raise ValueError(f"The parameter isClass must be '', 'function' or 'class' but you pass '{isClass}'")
    
    def main(self) -> None:
        if self.new.result == None:
            for c in range(0, len(self.new.tm)):
                self.result += self.new.tm[c]
                cod = ''
                try:
                    cod = self.new.tl[c]
                except IndexError:
                    pass
                try:
                    exec(compile(cod, '<string>', 'exec'), {
                        "TPRINT": lambda string: self.addT(string),
                        "PRINT": lambda string: self.addT(string),
                        "GET": lambda string: self.req.get(string),
                        "setGlobal": lambda var, value, isClass='': self.setGlobal(var,value, isClass),
                        "getGlobal": lambda var:  self.getGlobal(var)
                    })
                except Exception as error:
                    res : str = Error(error, cod.split('\n')).log()
                    print(res)
                    self.result = f"""
                        <h1>Teddy Error</h1>
                        <ul>
                            <li>{res}</li>
                            <li>Check terminal</li>
                            <li>Restart the terminal</li>
                        <ul>
                    """
                    return
        else:    
            print(self.new.result)
            self.result = f"""
                <h1>Teddy Error</h1>
                <ul>
                    <li>{self.new.result}</li>
                    <li>Check terminal</li>
                    <li>Restart the server</li>
                <ul>
            """
            return



def start(string : str, terminal : bool = False, port : int = 5000) -> None:        
    
    new : ex.Inter = ex.Inter(string, keywords.keywords,keywords.pythonEqual)
    routes : getUrls.Url = getUrls.Url(string)
    urls : str = routes.line
    mainRoute = RemoveTag(new.tm, 'include')
    new.tm = mainRoute.result
    
    @app.route('/')
    def MainRoute() -> str:
        result = run(terminal, new, request.args)
        return result.result
    
    def convert(list) -> list[str]:
        res = []
        for c in range(0, len(list)):
            res.append(exe(list[c]))
        return res
    
    def elimenate(list, char) -> list[str]:
        new = []
        for c in range(0, len(list)):
            if list[c].strip() == char:
                continue
            else:
                new.append(list[c])
        return new
        
    
    new.tm = convert(new.tm)
 
    def NewRoute(name : str, method, file) -> None:
        global count
        count += 1
        program = f"'{open(file, 'r', encoding='utf-8').read()}'"
        programNew = ex.Inter(program, keywords.keywords,keywords.pythonEqual)
        programNew.tm[0] = programNew.tm[0][1:]
        programNew.tm = convert(programNew.tm)
        programNew.tm = elimenate(programNew.tm, '')
        programNew.tm[-1] = programNew.tm[-1][-1]
        programNew.tm = elimenate(programNew.tm, "'")
        
        r = Optimaze([f'@app.route("/{name}", methods={method})\ndef NewRoute{count}() -> str:\n     return run({terminal}, programNew, request.args).result']).result[0]
        exec(r,{
            "programNew": programNew,
            "request": request,
            "app": app,
            "run": run
        })
       
    if not urls == '':
        for k,v in eval(urls).items():
            NewRoute(k, eval(urls)[k]["method"], eval(urls)[k]["file"])
       
    if not terminal:
        try:
            app.run(host='localhost', port=port)
        except RuntimeError:
            print("Runtime Error: there is a server running in this port")