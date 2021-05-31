import lexical
import Tparser
import get

class Inter:
    
    def __init__(self, code : str, keywords : list, pythonkey : dict):
        self.pythonkey : dict = pythonkey
        self.code  : str = code
        self.keywords : list = keywords
        self.result = None
        self.get = get.get(code + '<teddy></teddy>')
        self.tm : list[str] = self.get.getMark()
        self.tl : list[str] = self.get.getLanguage()
        self.parse()
        
    def parse(self) -> None:
        for c in self.tl:
            p = Tparser.Parser(self.code, self.keywords)
            if p.result is not None:
                self.result = p.result
                return
        self.lexical()
                
    def lexical(self) -> None:
        for c in range(0, len(self.tl)):
            self.tl[c] = lexical.lexical(self.tl[c], self.pythonkey, self.keywords).code