from html.parser import HTMLParser as HTML

class html(HTML):
        
    def __init__(self, line):
        super().__init__()
        self.teddy = False
        self.html = ''
        self.line = line
        self.count = -1
        self.total = 0
        self.last = 0
        self.tl = []
        self.tm = []
        super().feed(self.line)
        self.whenFinish()
    
    def return_tag(self, tag, attrs=None):
        if attrs is None:
            a = f"<{tag}"
            for atr in attrs:
                a += f'{atr[0]}="{atr[1]}"'
            a += f">"
            return a
        else:
            a = f"</{tag}>"
            return a
            
    def handle_starttag(self, tag, attrs):
        a = self.return_tag(tag, attrs)
        if tag == 'teddy':
            self.count += 1
            self.tl.append('')
            self.tm.append(self.line[self.last:self.total-1])
            self.total += len(a)
            self.last = self.total
            self.teddy = True
        else:
            self.total += len(a)
        
    def handle_data(self,data):
        if self.teddy:
            self.tl[self.count] += data
        self.last = self.total
        self.total += len(data)
        
    def handle_endtag(self,data):
        self.teddy = False
        self.last = self.total
        self.total += len(f"</{data}>")
        
    def whenFinish(self):
        self.tm.append(self.line[self.last:self.total])