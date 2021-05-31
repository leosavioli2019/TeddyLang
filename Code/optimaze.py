class Optimaze:
    
    def __init__(self, list):
        self.list = list
        self.result = []
        self.main()
        
    def main(self):
        for c in range(0, len(self.list)):
            self.result.append(compile(self.list[c], '<string>', 'exec'))
            