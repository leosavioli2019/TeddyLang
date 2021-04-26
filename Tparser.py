import system
import util 

class Parser:
    
    def __init__(self,code,keywords):
        self.code = code
        self.lines = code.split('\n')
        self.keywords = keywords
        self.result = None
        self.fofError()
        
    def fofError(self):
        error = system.error(self.code, '"')
        if error == None:
            error = system.error(self.code, "'")
            if error == None:
                self.repeatError()
            else:
                self.result = error    
        else:
            self.result = error

    def repeatError(self):
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
            
    def doError(self):
        do = len(util.replace(self.code,'do','do', True)[1])
        end = len(util.replace(self.code,'end','end', True)[1])
        if do == end:
            return
        else:
            if do > end:
                self.result = f"Syntax Error: there are {end} end and {do} do is missing {do-end} end"
            else:
                self.result = f"Syntax Error: there are {do} do and {end} end is missing {end-do} end"