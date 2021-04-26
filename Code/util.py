import system

def findAll(word,line,l=[]):
    if not(word in line):
        return l
    else:
        after = line[line.find(word):]
        end = l 
        end.append(line.find(word))
        return end if not(word in after) else findAll(word,after,end)
    
def replace(string, char1, char2, chan=False):
    result = string 
    changes = []
    for c in range(0, len(string)):
        if string[c:c+len(char1)] == char1 and not(system.test(string, c, '"')) and not(system.test(string, c, "'")):
            changes.append(c)
    for c2 in changes:
        result = result[:c2-1] + char2 + result[c2+len(char1):]
    return [result,changes] if chan else result