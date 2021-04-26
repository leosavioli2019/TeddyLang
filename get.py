import teddymark.getcode as code

class get:
    
    def __init__(self, line):
        self.line = line
        self.code = code.html(line)
        self.language = self.code.tl
        self.mark = self.code.tm 
    
    def getLanguage(self):
        return self.language

    def getMark(self):
        return self.mark       