import util 

class lexical:
    
    def __init__(self, code, keys, keywords):
        self.code = code
        self.list = self.code.split('\n')
        self.keys = keys
        self.keywords = keywords
        self.inter()
        
    def list_str(self):
        self.code = ''
        for c in self.list:
            self.code += f"{c}\n"
    
    def inter(self):
        for key, value in self.keys.items():
            string, lists = util.replace(self.code, key, value, True)         
            self.code = string
        self.list = self.code.split('\n')
        self.indentation()
        
    def indentation(self):
        indent = 0        
        for c in range(0, len(self.list)):
            if not self.list[c].strip() == '':
                indent = len(self.list[c]) - len(self.list[c].lstrip())
                break
        if indent == 0:
            return
        else:
            for c in range(0, len(self.list)):
                self.list[c] = self.list[c][indent:]
            self.list_str()