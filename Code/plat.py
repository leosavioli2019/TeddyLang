import sys

def route() -> str:
    if sys.platform == 'win32':
        return "\\"
    elif sys.platform == 'darwin':
        return "/"    
    elif sys.platform == 'linux':
        return "/"