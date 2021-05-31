from console import console
import sys

class App(console):
    
    def __init__(self,args, options):
        self.args = args
        self.options = options
        super().__init__()
        self.argv()
    
    def terminal(self):
        for c in range(0, len(self.args)):
            if self.args[c] == '--terminal':
                try:
                    self.compile(self.args[c+1], True)
                except IndexError:
                    try:
                        self.compile(self.args[c-1], True)
                    except IndexError:
                        self.t.help()   
                        
    def build(self):
        for c in range(0, len(self.args)):
            if self.args[c] == 'build':
                try:
                    platform = self.args[c+1]
                    if not platform in self.options:
                        self.t.help()
                        return
                    file = self.args[c+2]
                except IndexError:
                    self.t.help()
                    return
                else: 
                    if platform == 'web':
                        self.compile(file) 

        
    def argv(self):
        if '--help' in self.args:
            self.t.help()      
        elif 'build' in self.args:
            self.build()
        elif '--version' in self.args:
            print(self.t.__version__)
        else:
            self.t.help()
            
App(sys.argv, ["web"])