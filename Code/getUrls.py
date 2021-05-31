from html.parser import HTMLParser as HTML
import plat

class Url(HTML):
    
    def __init__(self, line):
        super().__init__()
        self.line = ''
        self.getData = False
        self.text = ''
        self.list = []
        self.ev = None
        self.form = []
        self.feed(line)
        
    def file(self, filename):    
        port = filename[:filename.find(".")]
        return port
    
    def list_str(self):
        self.line = ''
        for c in range(0, len(self.list)):
            self.line += f"{self.list[c]}\n"
    
    def ConvertToListType(self, dicts):
        newList = []
        newDict = {}
        for k ,v in dicts.items():
            newDict["rout"] = k
            newDict["method"] = dicts[k]["method"]
            newList.append(newDict)
            newDict = {}
        return newDict
    
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
    
    def handle_starttag(self, tag, attrs):
        if tag == "include":
            self.getData = True
        else:
            self.getData = False

    def handle_data(self, data):
        if self.getData:
            self.line = data
            self.list = data.split('\n')
            self.indentation()
            self.line = "{" + self.line + "}"
            self.getData = False

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        
        
