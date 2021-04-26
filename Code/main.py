from console import console
import sys

class App(console):
    
    def __init__(self,args):
        self.args = args
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
        
    def argv(self):
        if '--imp' in self.args:
            self.main()
        elif '--help' in self.args:
            self.t.help()
        elif '--terminal' in self.args:
            self.terminal()
        else:
            self.t.help()
            
App(sys.argv)