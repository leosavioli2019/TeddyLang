class html:
    
    def __init__(self, line) -> None: #("# oi # <teddy>oi</teddy> # oi # <teddy>5</teddy> %")
        self.line = line
        self.tm = []
        self.tl = []
        self.start(self.line + ' ')
        
    def start(self, line):
        before = line[:line.find('<teddy>')]
        # "# oi #"
        self.tm.append(before)
        
        l = line.find('</teddy>')+8
        # :"# oi # <teddy>5</teddy> %"
        
        var = line[l:]
        # " # oi # <teddy>5</teddy> %"
        
        after = var[:var.find('<teddy>')]
        # " # oi # "
        
        
        self.tm.append(after)
        if not line.find('<teddy>') == -1:
            self.tl.append(line[line.find('<teddy>')+7:line.find('</teddy>')])
        if '<teddy>' in var: # "<teddy>5</teddy> %""
            self.tm.append(self.start(var[len(after):]))
        else:
            return after
        