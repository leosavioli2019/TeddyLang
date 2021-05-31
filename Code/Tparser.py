import system
import util 
import lexer

class Parser:
    
    def __init__(self,code : str, keywords : list):
        self.code : str = code
        self.lines : list = code.split('\n')
        self.keywords : list = keywords
        self.result = None
        self.fofError()
        
    def fofError(self) -> None:
        error = system.error(self.code, '"')
        if error == None:
            error = system.error(self.code, "'")
            if error == None:
                self.pythonEnd()
            else:
                self.result = error    
        else:
            self.result = error

    def pythonEnd(self) -> None:
        for key in self.keywords:
            for c in range(0, len(self.lines)):
                if util.replace(self.lines[c], key, key, True)[1] != [] and self.lines[c][-2:] != "do":
                    self.result = f"Syntax Error: you have to finish the loop line with a do"
                    return
        self.elseError()
        
    def elseError(self):
        e = lexer.elseError(self.code)
        if e.result != None:
            self.result = e.result
        else:
            self.repeatError()
    
    def repeatError(self) -> None:
        for key in self.keywords:
            for c in range(0,len(self.lines)):
                wordKey = len(util.replace(self.lines[c],key,key,True)[1])
                do = len(util.replace(self.lines[c],'do','do',True)[1])
                if wordKey == 0:
                    continue
                if wordKey == do and wordKey <= 1:
                    self.doError()
                else:
                    if wordKey == do:
                        self.result = f"Syntax Error: you can only put one conditional in a line but there are {wordKey} {key}"
                    elif wordKey > 1:
                        self.result = f"Syntax Error: there are {wordKey} {key}, but you can onpy put one {key} in a line"
                    elif do > wordKey:
                        self.result = f"Syntax error: there are {wordKey} {key}, but {do} do."
                    elif do < wordKey:
                        self.result = f"Syntax error: there are {wordKey} {key}, but only {do} do."
            
    def doError(self) -> None:
        do = len(util.replace(self.code,'do','do', True)[1])
        end = len(util.replace(self.code,'end','end', True)[1])
        if do == end:
            return
        else:
            if do > end:
                self.result = f"Syntax Error: there are {end} end and {do} do is missing {do-end} end"
            else:
                self.result = f"Syntax Error: there are {do} do and {end} end is missing {end-do} end"