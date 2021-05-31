import util

class elsif:
    
    def __init__(self, code):
        self.code = code
        self.result = []
        self.elsifConverter()

    def elsifConverter(self):
        for c in range(0, len(self.code)):
            pos = util.replace(self.code[c], 'elsif', 'elsif', True)[1]
            if pos != []:
                self.code[c] += ':'
        self.elseConvert()
                
    def elseConvert(self):
        for c in range(0, len(self.code)):
            pos = util.replace(self.code[c], 'else', 'else', True)[1]
            if pos != []:
                self.code[c] += ':'