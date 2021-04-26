import lexical
import Tparser
import get

class Inter:
    
    def __init__(self, code, keywords, pythonkey):
        self.pythonkey = pythonkey
        self.code = code
        self.keywords = keywords
        self.result = None
        self.get = get.get(code)
        self.tm = self.get.getMark()
        self.tl = self.get.getLanguage()
        self.parse()
        
    def parse(self):
        for c in self.tl:
            p = Tparser.Parser(self.code, self.keywords)
            if p.result is not None:
                self.result = p.result
                return
        self.lexical()
                
    def lexical(self):
        for c in range(0, len(self.tl)):
            self.tl[c] = lexical.lexical(self.tl[c], self.pythonkey, self.keywords).code