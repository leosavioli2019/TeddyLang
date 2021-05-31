def PRINT(string : str) ->  None:
    pass

def TPRINT(string : str) -> None:
    pass

class Error:
    
    def __init__(self, exception, code : list):
        self.exception = exception
        self.code : list = code
        
    def getLine(self, error) -> int:
        for c in range(0, len(self.code)):
            try:
                exec(self.code[c])
            except Exception as e:
                if f"{e}" == f"{error}":
                    return c
                    
    def log(self) -> str:
        line = self.getLine(self.exception)
        if line is None:
            line = ''
        else:
            line = 'in line '+str(line)
        if self.exception.__class__ == NameError:
            return f"Invalid Name: {self.exception} {line}"
        elif self.exception.__class__ == TypeError:
            return f"Type Error: {self.exception} {line}"
        elif self.exception.__class__ == ZeroDivisionError:
            return f"Division by Zero: you can not do a division by zero but there is {line}"
        elif self.exception.__class__ == IndexError:
            return f"Index Error: {self.exception} {line}"
        elif self.exception.__class__ == KeyError:
            return f"key Error: {self.exception} {line}"
        elif self.exception.__class__ == ValueError:
            return f"value Error: {self.exception} {line}"
        elif self.exception.__class__ == MemoryError:
            return f"Memory Error: {self.exception} {line}"
        elif self.exception.__class__ == IndentationError:
            return f"Indentation Error: {self.exception} {line}"
        elif self.exception.__class__ == SyntaxError:
            return f"Invalid Syntax: {self.exception} {line}"
        else:
            return f"{self.exception.__class__}: {self.exception} {line}"