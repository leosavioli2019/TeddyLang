import util

class elseError:
    
    def __init__(self, code):
        self.code = code
        self.result = None
        
    def ElseKeyWordError(self):
        for c in range(0, len(self.code)):
            __, pos = util.replace(self.code, 'elif', 'elif')
            if pos != []:
                self.result = """
                Syntax Error: you con not use python elif keyword in Teddy, 
                please try to replace elif to elsif the correct Teddy syntax"""
        
    def DoElseError(self):
        for c in range(0, len(self.code)):
            DoIn, ElseIn = util.replace(self.code, "else", "else")[1], util.replace(self.code, "do", "do")[1] 
            if ElseIn != [] and DoIn != []:
                self.result = "Syntax Error: in else you don't use do"
                
    def DoElsifError(self):
        for c in range(0, len(self.code)):
            DoIn, ElseIn = util.replace(self.code, "elsif", "elsif")[1], util.replace(self.code, "do", "do")[1] 
            if ElseIn != [] and DoIn != []:
                self.result = "Syntax Error: in elsif you don't use do"