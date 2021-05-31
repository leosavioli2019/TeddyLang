import re

class RemoveTag:
    
    def __init__(self, list, tag):
        self.list = list
        self.tag = tag
        self.result = []
        self.main()
        
    def main(self):
        newList = self.list
        for c in range(0, len(newList)):
            newList[c] = self.convert(newList[c])
        self.result = newList
        
    def convert(self, list):
        options = r".*"
        exp = f"<{self.tag}>{options}</{self.tag}>"
        return re.sub(exp, '', list)